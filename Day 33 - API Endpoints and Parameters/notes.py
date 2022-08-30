# Module for API requests
import requests

# setting the api call to a variable
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# will print error to screen if request is unsuccessful
response.raise_for_status()

# setting the json data from API call to variable
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")
# print(response.status_code)

#   404 - endpoint doesn't exist/ not found
#   1XX - Hold On
#   2XX - Success
#   3XX - Permission not granted
#   4XX - Front End error
#   5XX - Back End error (server, etc)

