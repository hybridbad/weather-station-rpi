from weather_data_mock import *
import json
import requests

class WeatherDataSender:

  api_url = 'https://fb724921.ngrok.io/api/data'

  def __init__(self, weather_data_mock = WeatherDataMock()):
    self.weather = weather_data_mock

  def pushData(self):
    data_string = json.dumps(self.weather.get())
    print("PUSHing data to %s" %(self.api_url))
    response = requests.post(self.api_url, data={'data': data_string})
    print(response)