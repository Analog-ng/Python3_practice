import requests

url = "http://api.weatherapi.com/v1/current.json?key=6c9cefe8b7ec49f2b95235448260211&q=Lagos&aqi=no"
response = requests.get(url)
weather_data = response.json()

location = weather_data["location"]["name"]
country = weather_data["location"]["country"]
local_time = weather_data["location"]["localtime"]
temperature_c = weather_data["current"]["temp_c"]
condition = weather_data["current"]["condition"]["text"]

print(f"Location: {location}, {country}")
print(f"Local Time: {local_time}")
print(f"Temperature: {temperature_c}°C")
print(f"Condition: {condition}")