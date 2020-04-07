  
import urllib.request
import json
import pprint

APIKEY = 'b478807d63589446d600b9e74d595ca3'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# pprint.pprint(response_data)
pprint.pprint(response_data['main']['temp'])
tempK = response_data['main']['temp']
tempF = round((tempK - 273.15) * (9/5) + 32)
print(f'The temperature in Wellesley is {tempF}°F')
