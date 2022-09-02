import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "STOCK_API_KEY"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
    }

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_API_KEY"
NEWS_PARAMETERS ={
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
}

ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "TWILIO_AUTH_TOKEN"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. 
# [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for(key, value) in stock_data.items()]
yesterday_info = stock_list[0]
yesterday_close = float(yesterday_info["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
two_day_ago_info = stock_list[1]
two_day_ago_close = float(two_day_ago_info["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, 
# but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
aboslute_difference = round(abs(yesterday_close - two_day_ago_close), 2)
up_down = None
if aboslute_difference > 5:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_difference = round(((aboslute_difference / yesterday_close) * 100), 2)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. 
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
if percent_difference < 5:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_slice = news_data[:3]
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension. 
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_difference}%\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in news_slice]

#TODO 9. - Send each article as a separate message via Twilio.     
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:

        message = client.messages \
            .create(
            body=article,
            from_='TWILIO_NUMBER',
            to='YOUR_NUMBER'
        )
        print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

