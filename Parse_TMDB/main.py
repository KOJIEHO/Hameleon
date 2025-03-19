from config import API_KEY, URL
import requests

import sys
sys.path.append("PLIB")

# TODO
# 1. Запись FileBlobb изображения

# ИДЕИ ФУНКЦИОНАЛА:
# 1. Функция парсинга прокси с какого-нибудь сайта
# 2. Сделать запись в файл id фильмов, о которых не было информации


# Функция проверки работоспособности прокси из файла
# Функция возвращает один работающий прокси из списка
def proxies_update():
    with open('proxies_list.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        url = "https://api.themoviedb.org/3/authentication"
        proxies = {'https': f'http://{line.strip()}'}
        headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200: 
                # print(f'Из списка подошел прокси:\n"http://{line.strip()}"')
                return proxies
            else: 
                print('Ошибка в запросе:')
                print(response.text)
        except Exception as inst:
            pass
    # print('Все прокси из файла не работают, попробуйте их обновить')


# Функция записи информации о фильме в БД
def post_info():
    pass


# Основная функция
# Пробегаем по всем id из файла и получаем информацию о фильмах
# Записываем информацию в БД Хамелеона
def main():
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    proxie = proxies_update()
    if proxie == None:
        print('Все прокси из файла не работают, попробуйте их обновить')
        return

    with open('id_list.txt', 'r', encoding='utf-8') as file:
        id_films = file.readlines()
    for id_film in id_films:
        id_film = id_film.strip()
        
        url = f"https://api.themoviedb.org/3/movie/{id_film}?language=ru_RU"

        # Пытаемся получать информацию о фильмах, id которых были в списке
        try:
            response = requests.get(url, headers=headers, proxies=proxie)
            print(f'Получили информацию о фильме {id_film},   СТАТУС КОД = {response.status_code}')
            if  response.status_code == 200:
                json = response.json()
                # print(json)
                print(type(json))
                data_message = [{
					"$type": "Film",
					"JSON_card": json,
					"adult": json['adult'],
					"backdrop_path": json["backdrop_path"],
					# "backdrop_IMG": ,
					"budget": json["budget"],
					"homepage": json["homepage"],
					# "cub_id": ,
					"imdb_id": json["imdb_id"],
					"origin_country": json["origin_country"],
					"original_language": json["original_language"],
					"original_title": json["original_title"],
					"overview": json["overview"],
					"popularity": json["popularity"],
					"poster_path": json["poster_path"],
					# "poster_IMG": ,
					"release_date": json["release_date"],
					"revenue": json["revenue"],
					"runtime": json["runtime"],
					"status": json["status"],
					"tagline": json["tagline"],
					"title": json["title"],
					"video": json["video"],
					"vote_average": json["vote_average"],
					"vote_count": json["vote_count"] 
					# "release_date_first": ,
					# "external_id": ,
					# "names_mas": ,
					# "kinopoisk_id": ,
					# "kp_rating": ,
					# "imdb_rating": ,
					# "release_quality": ,
					# "last_air_date": , 
				}]
                response_post_ham = requests.post(f'{URL}/ham/odata/Film', json=data_message)
                print(f'ФИЛЬМ ID = {id_film},   СТАТУС КОД = {response_post_ham.status_code}')
            elif response.status_code == 404:
                print(f'Информации о фильме с ID = {id_film} не найдена')         
        except Exception as inst:
            print('Видимо прокси перестал работать, обновите его')

            # print('Видимо прокси успел перестать работать, попробуем обновить')
            # proxie = proxies_update()


print(main())



# ----------------------------------------------------------------------------
# Пример json, который приходит с TMDB
# json = {
#     "adult": False,
#     "backdrop_path": "/hQ4pYsIbP22TMXOUdSfC2mjWrO0.jpg",
#     "belongs_to_collection": {
#         "id": 1382526,
#         "name": "Aki Kaurismäki's Proletariat Trilogy",
#         "poster_path": "/bUrReoZFLGti6ehkBW0xw8f12MT.jpg",
#         "backdrop_path": "/zAUItK1Nr473DIe8gWMsZ0DMR7L.jpg",
#     },
#     "budget": 0,
#     "genres": [
#         {"id": 35, "name": "Comedy"},
#         {"id": 18, "name": "Drama"},
#         {"id": 10749, "name": "Romance"},
#         {"id": 80, "name": "Crime"},
#     ],
#     "homepage": "",
#     "id": 2,
#     "imdb_id": "tt0094675",
#     "origin_country": ["FI"],
#     "original_language": "fi",
#     "original_title": "Ariel",
#     "overview": "A Finnish man goes to the city to find a job after the mine where he worked is closed and his father commits suicide.",
#     "popularity": 4.28,
#     "poster_path": "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg",
#     "production_companies": [
#         {
#             "id": 2303,
#             "logo_path": None,
#             "name": "Villealfa Filmproductions",
#             "origin_country": "FI",
#         }
#     ],
#     "production_countries": [{"iso_3166_1": "FI", "name": "Finland"}],
#     "release_date": "1988-10-21",
#     "revenue": 0,
#     "runtime": 73,
#     "spoken_languages": [
#         {"english_name": "Finnish", "iso_639_1": "fi", "name": "suomi"}
#     ],
#     "status": "Released",
#     "tagline": "",
#     "title": "Ariel",
#     "video": False,
#     "vote_average": 7.124,
#     "vote_count": 344,
# }
# print(json["adult"])



# ----------------------------------------------------------------------------
# URL для скачивания фотографий
# url = 'https://image.tmdb.org/t/p/w500/dsHWBit2DkXohujpBIJL7ftPUQF.jpg'

# proxies = {'https': 'http://67.43.236.21:31129'}
# headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
# response = requests.get(url, headers=headers, proxies=proxies)

# img_file = open('photo_original.jpg', 'wb')
# img_file.write(response.content)
# img_file.close()
