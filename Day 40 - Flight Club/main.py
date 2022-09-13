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

CRED_FILE = "C:/Users/bryan/Desktop/AWS/Portfolio/Python/100 Days of Python/flight-deals-361722-ebd7f965d000.json"
GOOGLE_SPREADSHEET_ID = os.environ.get("GOOGLE_SPREADSHEET_ID")

gc = gspread.service_account(CRED_FILE)
database = gc.open("Flight Deals")
wks = database.worksheet("users")
wks.get_all_records()

print("Welcome to Bryant's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()
user_email = input("What is your email address?\n")
verify_email = input("Please verify your email address\n")

if user_email == verify_email:
    print("You're in the club!")
else:
    user_email = input("Email does not match. Please re-enter email\n")

wks.update_cell(2,1,first_name)
wks.update_cell(2,2,last_name)
wks.update_cell(2,3,user_email)