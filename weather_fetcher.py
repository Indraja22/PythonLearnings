import os
import requests

API_KEY = os.getenv('WEATHER_API_KEY')

BASE_URL = "https://api.tomorrow.io/v4/weather/realtime"

city = input("Enter a city name : ")
request_url = f"{BASE_URL}?apikey={API_KEY}&location={city}"

response = requests.get(request_url, timeout=100)
response_as_json = response.json()
assert response.status_code == 200

print(response_as_json)
temperature = response_as_json['data']['values']['temperature']
print(f"Temperature in {city} is {temperature}°C")
