import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
GEO_API_URL = "https://geocoding-api.open-meteo.com/v1/search"

def process_location(location: str) -> dict:
    latitude, longitude = get_coordinates(location)
    return process_coordinates(location=location, latitude=latitude, longitude=longitude)

def get_coordinates(location: str) -> tuple[float, float]:
    params = {
        "name": location,
        "count": 1
    }
    responses = requests.get(GEO_API_URL, params=params, verify=False)
    if responses.status_code == 200:
        if "results" not in responses.json().keys():
            return (None, None)
        location = responses.json()["results"][0]
        return location["latitude"], location["longitude"]
    return (None, None)

def process_coordinates(location: str, latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max"]
    }
    responses = requests.get(OPEN_METEO_URL, params=params, verify=False)
    if responses.status_code == 200:
        return responses.json()
    return dict()
