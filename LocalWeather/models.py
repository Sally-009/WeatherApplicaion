from django.db import models
import requests
import json

class currentConditions():
    url = "https://api.weather.gov/gridpoints/LZK/35,93/forecast"
    # the entire data of this API
    returnData = requests.get(url).json()
    # properties in the entire data
    properties = returnData['properties']
    # periods in properties
    periods = properties['periods']
    