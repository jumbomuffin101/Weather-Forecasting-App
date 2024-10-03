import requests

# Your unique API key to access the OpenWeatherMap API
API_KEY = 'e07a3c83cf368475b5a9a1dbe22c24e6'
# Base URL for fetching weather data
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Fetches and displays the current weather information for a specified city."""
    
    # Constructing the request URL using the city name
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    # Sending a request to the OpenWeather API to get the weather data
    response = requests.get(request_url)
    
    # Checking if we received a successful response
    if response.status_code == 200:
        # Parsing the response data from JSON format
        data = response.json()
        
        # Extracting relevant weather details
        main = data['main']
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        # Printing the weather details in a friendly format
        print(f"\n🌤️ Weather in {city.capitalize()}:")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"🤗 Feels Like: {feels_like}°C")
        print(f"☁️ Weather Condition: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")
    else:
        # If the city was not found, let the user know
        print(f"🚫 Oops! I couldn't find the weather for '{city}'. Please check the city name and try again.")

if __name__ == "__main__":
    print("👋 Welcome to the Weather Forecasting App! Let's check the weather together!")
    
    # Asking the user to enter the name of a city
    city = input("🌆 Please enter the name of a city: ")
    
    # Calling the function to fetch and display the weather data
    get_weather(city)
