from django.db import models
import requests
import json

class currentConditions():
    url = "https://api.weather.gov/gridpoints/LZK/35,93/forecast"
    returnData = requests.get(url).json()