import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json#")
response.raise_for_status()

data = response.json()

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
iss_coordinates = (latitude, longitude)

print(f"The ISS coordinates are: {iss_coordinates}")
