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

CRED_FILE = "Day 39 - Flight Deal Finder\\flight-deals-361722-ebd7f965d000.json"
gc = gspread.service_account(CRED_FILE)

print("Welcome to Bryant's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()
user_email = input("What is your email address?\n")
verify_email = input("Please verify your email address\n")

if user_email == verify_email:
    print("You're in the club!")
else:
    user_email = input("Email does not match. Please re-enter email\n")