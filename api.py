import requests


def getUrl(baseUrl):

    url = "https://instagram-downloader.p.rapidapi.com/index"

    querystring = {"url":baseUrl}

    headers = {
        "x-rapidapi-key": "48df05ae39msh3a009153a99364ep1270e6jsn66728f865c47",
        "x-rapidapi-host": "instagram-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()['result']['video_url']