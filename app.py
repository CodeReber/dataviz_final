import requests
from pprint import pprint

parameters = {
    "Authorization": '5897db64d0634bc43bfbfffb738fd1b7ed0104da'
}

url = "https://app.climate.azavea.com/api/scenario/"

response = requests.get(url, headers={'Authorization': 'Token 5897db64d0634bc43bfbfffb738fd1b7ed0104da'})


pprint(response.json())