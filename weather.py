import requests
city = input("What city would you like to know the weather from? :\n")
url = 'http://api.weatherapi.com/v1/current.json?key=d8b8176458bf4fe680c235355240902&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

location = weather_json.get('location').get('name')
temp = weather_json.get('current').get('temp_c')
condition = weather_json.get('current').get('condition').get('text')
print(f'The temperature in {location} is {temp}c and the weather condition is {condition}')
