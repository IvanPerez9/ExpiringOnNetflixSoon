import requests


def get_expiring_per_country(country, api_key):
    url = "https://unogsng.p.rapidapi.com/expiring"
    querystring = {"countrylist": country}
    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    movie_dicts = data["results"]
    expiring_movies = {movie["title"]: movie["unogsdate"] for movie in movie_dicts}
    return expiring_movies