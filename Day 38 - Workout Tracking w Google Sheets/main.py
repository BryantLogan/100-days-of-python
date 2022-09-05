from datetime import date, datetime
import requests

APP_ID = "yourappid"
API_KEY = "yourapikey"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


SHEETY_POST_ENDPOINT = f"yoursheetyendpoint"

auth_info = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
EMAIL = {
    "name": "YourName",
    "email": "example@email.com",
    "canAttend": "true"
}

BASIC_AUTH = {
    "username": "username",
    "password": "password"}

sheety_headers = {
    "Authorization": "YourToken",
}

date_string = datetime.now()
todays_date = datetime.today().strftime("%d-%m-%Y")
time_now = datetime.today().strftime("%H:%M:%S")

user_input = input("Which exercises did you do?: ")
exercise = {
    "query": user_input
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=auth_info,json=exercise)
response.raise_for_status()
exercise_data = response.json()["exercises"][0]
workout_type = exercise_data["name"].title()
duration = exercise_data["duration_min"]
calories_burned = exercise_data["nf_calories"]

sheety_dict = {
    "workouts": {
        "date": todays_date,
        "time": time_now,
        "exercise": workout_type,
        "duration": duration,
        "calories": calories_burned,
    }
}

sheet_post = requests.post(url=SHEETY_POST_ENDPOINT,json=sheety_dict, headers=sheety_headers)
sheet_post.raise_for_status()