# Advanced-Weather-Data-Script
This script fetches the current weather data for a given location using the WeatherAPI and generates an email body that describes the weather conditions in a human-readable format using the Gemini AI.

## Installation

Before running the script, you need to install the required Python packages. You can do this by running the following commands in your terminal:

```bash
pip3 install requests
pip3 install python-dotenv
pip3 install google-generativeai
```

# API Keys
You also need to obtain API keys from WeatherAPI and Gemini AI:

WeatherAPI: Sign up on the WeatherAPI website to get your API key.
Gemini AI: Sign in on the Gemini API developers page to get your API key.
Once you have your API keys, edit the .env file in the same directory as your script and add the following lines to it:

```bash
WEATHER_API_KEY=your_weather_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace your_weather_api_key and your_gemini_api_key with your actual API keys.

#Usage
To run the script, navigate to the directory containing the script in your terminal and run the following command:

```bash
python3 weather.py
```
