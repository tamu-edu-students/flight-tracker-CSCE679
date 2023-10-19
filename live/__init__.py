import requests

url = "https://sky-scanner3.p.rapidapi.com/languages"

headers = {
	"X-RapidAPI-Key": "18607e0d16msh608c9f7e2ea52cep1ea2cfjsnfbdd1a2fce9c",
	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}

def get_languages():
	response = requests.get(url, headers=headers)

	print(response.json())
	return response.json()