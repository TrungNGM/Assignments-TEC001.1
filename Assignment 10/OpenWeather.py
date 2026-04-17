import requests

city = input("Enter your municipality: ")

API_KEY = "e24a22b697bdc884d34958f828d00d6c"

request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(request).json()

if response.get("cod") == 200:
    description = response["weather"][0]["description"]
    temp_kelvin = response["main"]["temp"]

    temp_celsius = temp_kelvin - 273.15

    print("Weather:", description)
    print("Temperature:", round(temp_celsius, 2), "°C")

else:
    print("Error:", response.get("message"))