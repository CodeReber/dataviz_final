import requests
from pprint import pprint

parameters = {
    "lat": '39.95',
    "lon": '-75.16',
    "limit": '10'
}

url = "https://app.climate.azavea.com/api/city/nearest/"

response = requests.get(url, params=parameters, headers={'Authorization': 'Token 5897db64d0634bc43bfbfffb738fd1b7ed0104da'})


pprint(response.json())