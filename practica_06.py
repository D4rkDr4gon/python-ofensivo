import requests
import json

# Get the IP address from the user
ip_address = input("Enter an IP address: ")

# Make a GET request to the IP geolocation API
response = requests.get(f"https://ipapi.co/{ip_address}/json/")

# Parse the JSON response
data = json.loads(response.text)

# Check if the response contains the necessary information
if "country_name" in data and "city" in data and "latitude" in data and "longitude" in data:
    country = data["country_name"]
    city = data["city"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    # Print out the geolocation information
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Geolocation information not available for this IP address.")
