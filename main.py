import datetime as dt
import requests

# Base URL of the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# API key for accessing the OpenWeatherMap API
API_KEY = "00000000000000000000000" // enter your API KEY here

# Function to convert temperature from Kelvin to Celsius and Fahrenheit
def kelvin_converter(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Function to display a header with ASCII art
def display_header():
    print("\n╔════════════════════════════════════════════════╗")
    print("║              Weather Forecast App              ║")
    print("╚════════════════════════════════════════════════╝")

# Prompt the user to input the country and city
country = input("Enter the country: ")
city = input("Enter the city: ")

# Construct the API request URL using the country, city, and API key
url = f"{BASE_URL}q={city},{country}&appid={API_KEY}"

# Send a GET request to the OpenWeatherMap API and parse the JSON response
response = requests.get(url).json()

# Display header
display_header()

# Check if the response contains a status code of 200, indicating a successful request
if response.get('cod') == 200:
    # Extract weather data from the response
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_converter(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_converter(feels_like_kelvin)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    # Convert sunrise and sunset times to local time
    timezone_offset = response['timezone']
    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz=dt.timezone(dt.timedelta(seconds=timezone_offset)))
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'], tz=dt.timezone(dt.timedelta(seconds=timezone_offset)))

    # Print weather information with descriptive labels
    print("\nWeather Information:")
    print(f"City: {city}, {country}")
    print(f"Description: {description}")
    print(f"Temperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")
    print(f"Feels like: {feels_like_celsius:.2f}°C / {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity: {humidity}%")
    print(f"Sunrise time: {sunrise_time.strftime('%H:%M:%S')} (local time)")
    print(f"Sunset time: {sunset_time.strftime('%H:%M:%S')} (local time)")
else:
    # Print a message if weather data retrieval failed
    print("Failed to retrieve weather data. Please check the country and city you entered.")
