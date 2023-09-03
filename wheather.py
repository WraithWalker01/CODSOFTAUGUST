import requests


def get_weather_data(city_or_zip, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_or_zip,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None


def display_weather(data):
    if data and data["cod"] == 200:
        weather = data["weather"][0]
        main = data["main"]
        wind = data["wind"]

        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Error: City not found.")


def main():
    api_key = "YOUR_API_KEY"
    user_input = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather_data(user_input, api_key)
    if weather_data:
        display_weather(weather_data)


if __name__ == "__main__":
    main()
