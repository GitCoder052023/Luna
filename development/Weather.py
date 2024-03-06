import requests
import pyttsx3

engine = pyttsx3.init()


def get_weather():
    api_key = "REPLACE WITH YOUR OWN API KEY"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Lucknow"

    complete_url = base_url + f"appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        current_temperature = main_info["temp"]
        current_pressure = main_info["pressure"]
        current_humidity = main_info["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Temperature (in Kelvin) = {current_temperature:.2f}")
        print(f"Atmospheric pressure (in hPa) = {current_pressure}")
        print(f"Humidity (in percentage) = {current_humidity}")
        print(f"Description: {weather_description}")

        engine.say(f"Temperature (in Kelvin) = {current_temperature:.2f}")
        engine.say(f"Atmospheric pressure (in hPa) = {current_pressure}")
        engine.say(f"Humidity (in percentage) = {current_humidity}")
        engine.say(f"Description: {weather_description}")
        engine.runAndWait()
