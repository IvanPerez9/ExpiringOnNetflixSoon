import requests


def get_expiring_per_country(api_key, country='ES'):
    """
    Get expiring movies and show from Netflix unnoficial API
    @param country: search expiring movies by country. ES default
    @param api_key: free api key from rapidapi
    @return: list of expiring movies and shows by country
    """
    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"
    querystring = {"q": "get:exp:" + country, "t": "ns", "st": "adv", "p": "1"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "unogs-unogs-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    if 200 is not response.status_code:
        print(data['message'])
        exit(1)
    movie_dicts = data["ITEMS"]
    # Just title and expiring date
    expiring_movies = {movie["title"]: movie["unogsdate"] for movie in movie_dicts}
    return expiring_movies