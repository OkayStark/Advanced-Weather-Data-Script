import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

WEATHER_KEY = os.getenv('WEATHER_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

class NoAPIKeyError(Exception):
    pass

class InvalidAPIKeyError(Exception):
    pass

class NoWeatherDataError(Exception):
    pass

class ServerError(Exception):
    pass

def fetch_weather_data(location):
    try:
        if not WEATHER_KEY:
            raise NoAPIKeyError("No weather API key provided.")
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={location}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise NoWeatherDataError("No weather data received.")
        return data
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 403:
            raise InvalidAPIKeyError("Invalid weather API key.")
        else:
            raise ServerError("An error occurred while fetching weather data.")

def generate_email(weather_data):
    try:
        if not GEMINI_API_KEY:
            raise NoAPIKeyError("No Gemini API key provided.")
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        convo = model.start_chat(history=[])
        weather_data_str = str(weather_data)
        convo.send_message(f"Generate an email body that describes the following weather conditions in a human-readable format: {weather_data_str}. The email should start with a greeting and end with a polite closing.")
        return convo.last.text.replace("[Name]", "User")
    except Exception as e:
        raise ServerError("An error occurred while generating the email.")

def main():
    location = input("Enter a location: ")
    try:
        weather_data = fetch_weather_data(location)
        email = generate_email(weather_data)
        print(email)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()