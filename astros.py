import requests

response = requests.get("https://api.open-notify.org/astros.json")
crew_members = response.json()

for member in crew_members["people"]:
    print(f"Name: {member['name']}, Craft: {member['craft']}")