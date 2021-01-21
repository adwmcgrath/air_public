import requests
import json
import os
from twilio.rest import Client

# set twilio environment variables (or for more security in the os path)

account_sid = 'x'
auth_token = 'x'


#function to create & send text 

def create_text():
	merge = get_data()
	body = str(merge)
	client = Client(account_sid, auth_token)
	client.api.account.messages.create(
	    to="x",
	    from_="x",
	    body=body)

# function to get the data from KCL API for Southwark. Hack around with the JSON to get PM10 & Nitrogen Dioxide readings.

def get_data():
	URL = 'http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode=SK5/JSON'
	page = requests.get(URL)
	dict =page.json()
	list = dict["DailyAirQualityIndex"]["LocalAuthority"]["Site"]["Species"]
	nox = (list[0])

	noxkeys = ['@SpeciesDescription', '@AirQualityBand','@AirQualityIndex']

	noxdata =[nox[x] for x in noxkeys]

	pm10 = (list[1])

	pm10keys = ['@SpeciesDescription', '@AirQualityBand','@AirQualityIndex']

	pm10data = [pm10[x] for x in pm10keys]

	return pm10data + noxdata

get_data()

create_text()
