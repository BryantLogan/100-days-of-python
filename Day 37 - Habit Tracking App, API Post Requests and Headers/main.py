import requests
from datetime import date as dt, datetime

USERNAME = "USERNAME"
TOKEN = "YOURTOKEN"
pixela_endpoint ="https://pixe.la/v1/users"
today = str(dt.today()).replace("-", "")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creates pixela account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph3",
    "name": "study-graph",
    "unit": "Days",
    "type": "int",
    "color": "ajisai",
}
# Creates a graph using graph_config params
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

create_pixel_config = {
    "date": today,
    "quantity": "1",
}

create_pixel_endpoint = f"{graph_endpoint}/graph1"

# Creates a pixel using create_pixel_config params
response = requests.post(url=create_pixel_endpoint, json=create_pixel_config, headers=headers)
print(response.text)





