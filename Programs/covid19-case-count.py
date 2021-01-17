import requests
import config

url = "https://covid-19-global-tracker-with-regional-data.p.rapidapi.com/api/covid/globalData"

headers = {
    'x-authorization': "6179002e-6646-4852-be37-572758a58cbb",
    'x-rapidapi-key': config.x_rapidapi_key,
    'x-rapidapi-host': "covid-19-global-tracker-with-regional-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

Cases = eval(response.text.replace('true','True'))['data']

for i in Cases:
    print(i)