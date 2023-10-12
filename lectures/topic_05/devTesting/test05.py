# API

# https://bank.gov.ua/ua/open-data/api-dev

import requests # pip install requests

# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?valcode=USD&date=20080401

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

#print(response.json())

for elem in response.json():
    print(elem['cc'], "  ", elem['rate'])

