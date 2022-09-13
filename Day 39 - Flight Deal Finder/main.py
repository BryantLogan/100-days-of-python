from __future__ import print_function
import gspread
import google.auth
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
from datetime import datetime, timedelta
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
from dotenv import load_dotenv
load_dotenv()

cities = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York", "San Francisco", "Cape Town"]
CRED_FILE = "C:\Users\\bryan\Desktop\AWS\Portfolio\Python\\100 Days of Python\\flight-deals-361722-ebd7f965d000.json"
gc = gspread.service_account(CRED_FILE)

tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
future_date = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")

database = gc.open("Flight Deals")
wks = database.worksheet("prices")
wks.get_all_records()


TEQUILA_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_HEADER = {
    "apikey": TEQUILA_KEY
}
TEQUILA_AFFIL_ID = os.environ.get("TEQUILA_AFFIL_ID")
GOOGLE_SPREADSHEET_ID = os.environ.get("GOOGLE_SPREADSHEET_ID")
ORIGIN_ID = "LHR"

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
YOUR_NUMBER = os.environ.get("MY_NUMBER")

def get_iata_code():
    '''Gets IATA Code and posts to Google Sheets'''
    row = 2
    column = 2
    for city in cities:
        destination = city
        SEARCH_TOKEN = {
            "term": destination
        }
        response = requests.get(url= TEQUILA_LOCATION_ENDPOINT, params=SEARCH_TOKEN, headers=TEQUILA_HEADER)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        wks.update_cell(row,column,iata_code)
        row += 1

def find_prices():
    '''Gets IATA code, checks flight prices, and then posts price to Google Sheets'''
    new_row = 2
    column = 3
    for city in cities:
        # Gets IATA code
        destination = city
        SEARCH_TOKEN = {
            "term": destination
        }
        response = requests.get(url= TEQUILA_LOCATION_ENDPOINT, params=SEARCH_TOKEN, headers=TEQUILA_HEADER)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]        
        BOOKING_TOKEN = {
            "fly_from": ORIGIN_ID,
            "fly_to": iata_code,
            "date_from": tomorrow,
            "date_to": future_date,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "USD"
        }
        # Gets prices and updates Google Sheet
        data = requests.get(url= TEQUILA_SEARCH_ENDPOINT, params=BOOKING_TOKEN, headers=TEQUILA_HEADER)
        data.raise_for_status()
        price_data = data.json()["data"][0]
        price = price_data["price"]
        wks.update_cell(new_row,column,price)
        new_row += 1
    
def check_prices():
    '''Gets IATA code, checks flight prices, compares previous prices, and sends text if price is lower'''
    new_row = 2
    column = 3
    for city in cities:
        # Gets IATA code
        destination = city
        SEARCH_TOKEN = {
            "term": destination
        }
        response = requests.get(url= TEQUILA_LOCATION_ENDPOINT, params=SEARCH_TOKEN, headers=TEQUILA_HEADER)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]        
        BOOKING_TOKEN = {
            "fly_from": ORIGIN_ID,
            "fly_to": iata_code,
            "date_from": tomorrow,
            "date_to": future_date,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "USD"
        }
        # Gets prices and updates Google Sheet
        data = requests.get(url= TEQUILA_SEARCH_ENDPOINT, params=BOOKING_TOKEN, headers=TEQUILA_HEADER)
        data.raise_for_status()
        price_data = data.json()["data"]
        price = price_data["price"]
        date_from = price["local_departure"].strftime("%d/%m/%Y")
        date_to = price["local_arrival"].strftime("%d/%m/%Y")
        print(date_from)

        if price < wks.cell(new_row,column).value:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)

                message = client.messages \
                    .create(
                    body=f"Low price alert! Only ${price} to fly from London-LHR to {city}-{iata_code}, from {date_from} to {date_to}!",
                    from_=TWILIO_NUMBER,
                    to=YOUR_NUMBER
                    )
        print(message.status)

        new_row += 1

        

# get_iata_code()
# find_prices()
check_prices()