import requests

def get_place_by_pin_code(zip_code):
    url = f"https://api.zippopotam.us/us/{zip_code}"
    response = requests.get(url,timeout=30)
    if response.status_code == 200:
        data = response.json()
        place_name = data['places'][0]['place name']
        print(place_name)
    else:
        print("Invalid Pin code! No Place Found")

get_place_by_pin_code("94105")
