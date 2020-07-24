#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys
appId = '1f3b67f087feb149a2f86238046b6ccb'

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py zipCode')
	sys.exit()

location = ' '.join(sys.argv[1:])

# Download the Json data from OpenWeatherMap.org API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=' % location + appId 
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
print(weatherData)
data = weatherData['weather']
print('Current weather in %s:' % (location))
print(data[0]['main'], "-", data[0]['description'])

temp = weatherData['main']
print("Temperature is:", int(temp['temp']-273.15), "°C &",int((temp['temp']- 273.15) * 9/5 + 32), "°F" )