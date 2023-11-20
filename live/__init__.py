import requests

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