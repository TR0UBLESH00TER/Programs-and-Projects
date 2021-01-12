"""
Code in config.py: 

x_rapidapi_key  = "your-x-rapidapi-key"
x_rapidapi_host = "your-x-rapidapi-host"
"""

"""
You can get 'x-rapidapi-key' and 'x-rapidapi-host' here:
https://rapidapi.com/community/api/urban-dictionary
"""

import requests
import config

def uddef(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":word}
    headers = {
    'x-rapidapi-key':  config.x_rapidapi_key,
    'x-rapidapi-host': config.x_rapidapi_host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(eval(response.text))

while True:
    uddef(input("Enter the word: "))
