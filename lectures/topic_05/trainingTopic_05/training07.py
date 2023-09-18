# API for different process
# https://minfin.com.ua/ua/developers/api/
# https://bank.gov.ua/ua/open-data/api-dev
# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json
# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?valcode=USD&date=20080901
# requests popular and very comonly use
# https://pypi.org/project/requests/

# pip install requests
# pip show requests

import requests
import sys # parameters specificat
import json # comes with python

#if len(sys.argv) != 2:
#    sys.exit() # some message need to be provided

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

#print(response.json())
#print(response.json()[0])
#print(response.json()[0]['rate'])
# curency exchange calculator could be implemented

# print(json.dumps(response.json(), indent=2))

for elem in response.json():
    print(elem['cc'], "  ", elem['rate'])

# curency exchange calculator could be implemented


