import requests

url = "https://genius-song-lyrics1.p.rapidapi.com/search"

querystring = {"q":"Все идёт по плану","per_page":"10","page":"1"}

headers = {
	"X-RapidAPI-Key": "7868891ccamsh9707919760c6431p181ac5jsn0807b8ba7827",
	"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

