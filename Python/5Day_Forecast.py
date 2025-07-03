pip install pymongo
print("PyMongo and its dependencies downloaded and installed successfully")

import requests
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime
import os
from pymongo import MongoClient
print("Packages loaded successfully")

# Setting up the OpenWeatherMap API Key as env variable
API_KEY = open('My_Weather_API.txt', 'r').read().strip()  # strip to remove newline
print("API_KEY:", API_KEY)

#API Endpoints
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
AIR_QUALITY_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

# Connecting to the NoSQL database (MongoDB)
client = MongoClient("mongodb://localhost:27017/")
db = client["weather_etl"]
print('Connection with ', db.name, ' is successful')

collection = db["forecast_3hr_5day"]
print(collection.name,' is successfully created')

# ✅ Scrape top 200 cities
def fetch_top_200_cities():
    url = "https://worldpopulationreview.com/cities"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    rows = soup.find("table").find("tbody").find_all("tr")
    data = [[r.find_all("td")[2].text.strip(), r.find_all("td")[3].text.strip()] for r in rows[:200]]
    df = pd.DataFrame(data, columns=["City", "Country"])
    return np.array(df["City"]), np.array(df["Country"])

# ✅ Get coordinates
def geocode_city(city, country):
    params = {"q": f"{city},{country}", "limit": 1, "appid": API_KEY}
    r = requests.get(GEOCODE_URL, params=params)
    if r.status_code == 200 and r.json():
        data = r.json()[0]
        return data["lat"], data["lon"]
    return None, None

# ✅ Get 3-hourly forecast
def fetch_forecast(lat, lon):
    params = {"lat": lat, "lon": lon, "units": "metric", "appid": API_KEY}
    r = requests.get(FORECAST_URL, params=params)
    return r.json().get("list", []) if r.status_code == 200 else []

# ✅ Get air quality
def fetch_air_quality(lat, lon):
    r = requests.get(AIR_QUALITY_URL, params={"lat": lat, "lon": lon, "appid": API_KEY})
    if r.status_code == 200:
        aqi_data = r.json().get("list", [{}])[0]
        comp = aqi_data.get("components", {})
        return {
            "aqi": aqi_data.get("main", {}).get("aqi", "N/A"),
            "pm2_5": comp.get("pm2_5", "N/A"),
            "pm10": comp.get("pm10", "N/A"),
            "co": comp.get("co", "N/A"),
            "no2": comp.get("no2", "N/A")
        }
    return {}

# ✅ Single ETL run
def run_once(cities, countries, run_id):
    docs = []
    for i, (city, country) in enumerate(zip(cities, countries)):
        print(f"[Run {run_id}] {i+1}/200: {city}, {country}")
        lat, lon = geocode_city(city, country)
        if lat is None: continue

        forecast_data = fetch_forecast(lat, lon)
        air_quality = fetch_air_quality(lat, lon)

        for hour in forecast_data:
            docs.append({
                "run_id": run_id,
                "city": city,
                "country": country,
                "timestamp_utc": hour["dt_txt"],
                "weather": {
                    "temp": hour["main"].get("temp"),
                    "feels_like": hour["main"].get("feels_like"),
                    "temp_min": hour["main"].get("temp_min"),
                    "temp_max": hour["main"].get("temp_max"),
                    "pressure": hour["main"].get("pressure"),
                    "humidity": hour["main"].get("humidity"),
                },
                "air_quality": air_quality
            })
        time.sleep(0.5)

    if docs:
        collection.insert_many(docs)
        print(f"Inserted {len(docs)} records.")
    else:
        print("No records to insert.")

# ✅ Main loop
def main():
    cities, countries = fetch_top_200_cities()
    run_id = 1
    while True:
        print(f"\nRun #{run_id} started at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
        run_once(cities, countries, run_id)
        print(f"Run {run_id} completed.\nSleeping for 6 hours...\n")
        run_id += 1
        time.sleep(21600)  # every 6 hours

if __name__ == "__main__":
    main()
