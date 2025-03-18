import requests

url = "https://tmdb.kurwa-bober.ninja/3/discover/movie?include_adult=false&include_video=false&language=ru-RU&page=1&sort_by=popularity.desc"
# url = "https://api.themoviedb.org/3/movie/changes?page=1"


headers = {
    "accept": "application/json",
}

response = requests.get(url, headers=headers)

print(response.text)