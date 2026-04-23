import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days=None, kind=None,):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ =="__main__":
    print(get_data(place="Tokyo"))