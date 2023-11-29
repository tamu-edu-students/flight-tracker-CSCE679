import requests
from flask import Flask, jsonify, request, session, render_template
import json
import pandas as pd
import ast

languages_url = "https://sky-scanner3.p.rapidapi.com/languages"
flight_url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getFlightDetails"

skyscanner_headers = {
	"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}

def get_languages():
	response = requests.get(languages_url, headers=skyscanner_headers)

	print(response.json())
	return response.json()


def query_flight():

	querystring = {"itineraryId":"135422402201235305980127122402201550","legs":"0","sessionId":"9eb73ffa206e4c268dbf6d03896eb584","adults":"1","currency":"USD"}

	skyscrapper_headers = {
		"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
		"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
	}

	response = requests.get(flight_url, headers=skyscrapper_headers, params=querystring)

	print(response.json())

def getNearestAirport():
	url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getNearByAirports"

	lat = request.form['lat']
	lng = request.form['lng']

	querystring = {"lat": lat,"lng":lng}
		
	headers = {
		"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
		"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	return response.json()

# def getFlightPrice():
# 	url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getPriceCalendar"

# 	src = request.form['src']
# 	dst = request.form['dst']
# 	date = request.form['date']

# 	querystring = {"originSkyId":src,"destinationSkyId":dst,"fromDate":date}

# 	headers = {
# 		"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
# 		"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
# 	}

# 	response = requests.get(url, headers=headers, params=querystring)

# 	print(response.json())

# 	return response.json()

def searchAirport(airport):
	url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

	querystring = {"query":airport}

	headers = {
		"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
		"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	# print(response.json())
	response = response.json()
	print(response)

	# data = json.dumps(response)
	# print(response["data"]["skyId"])
	# print(response['data']['entityId'])
	entityId = response['data'][0]['entityId']
	skyId = response['data'][0]['skyId']
	# data = json.loads(str(my_dict))
	# print(data)

	return skyId, entityId

def searchFlights(originId, dstId, originEntityID, dstEntityId, date, passengers, cabinClass):
	url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"

	querystring = {"originSkyId":originId,"destinationSkyId":dstId,"originEntityId":originEntityID,"destinationEntityId":dstEntityId,"date":date,"adults":passengers,"currency":"USD","market":"en-US","countryCode":"US","sortBy":"best","cabinClass":cabinClass}

	headers = {
		"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
		"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())

	return response.json()

def process_flight_data(src, dst, flight_data, budget):
	print(type(flight_data))
	data_for_plotting = []
	total_available_trips = len(flight_data['data']['itineraries'])
	for i in range(total_available_trips):
		# print(len(flight_data['data']['itineraries'][i]['legs']))
		# break
		stopCount = flight_data['data']['itineraries'][i]['legs'][0]["stopCount"]
		if(stopCount == 0):
			# print(flight_data['data']['itineraries'][i]['legs'][0]['durationInMinutes'])
			# print(flight_data['data']['itineraries'][i]['legs'][0]['carriers']['marketing'][0]['name'])
			# print(flight_data['data']['itineraries'][i]['price']['formatted'])
			tmp_data = [src, dst, flight_data['data']['itineraries'][i]['legs'][0]['durationInMinutes'], flight_data['data']['itineraries'][i]['legs'][0]['carriers']['marketing'][0]['name'], flight_data['data']['itineraries'][i]['price']['formatted']]
			if (float(budget) >= float(flight_data['data']['itineraries'][i]['price']['raw'])):
				data_for_plotting.append(tmp_data)
	
	print(data_for_plotting)
	return jsonify(flight_data,200)
	