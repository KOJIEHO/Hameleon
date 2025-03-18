import requests
from config import API_KEY
# url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ru-RU&page=1"

# url для получения информации о фильме
# url = "https://api.themoviedb.org/3/movie/696506?language=ru-RU"

url = "https://api.themoviedb.org/3/movie/11?language=ru-RU"


# url = 'https://image.tmdb.org/t/p/w500/dsHWBit2DkXohujpBIJL7ftPUQF.jpg'


proxies = {
   'https': 'http://67.43.236.21:31129'
}

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
try:
    response = requests.get(url, headers=headers, proxies=proxies)
    print(response.status_code)
    print(response.text)
except Exception as inst:
    print('Видимо прокси сломался((')


# url = 'https://httpbin.io/ip'
# response = requests.get(url, proxies=proxies)

# img_file = open('photo_original.jpg', 'wb')
# img_file.write(response.content)
# img_file.close()


