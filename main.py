import requests

url = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword'
api_key = '83ab7be7-a127-42b1-b2c2-09da98f0da7b'

film_name = input('Введите название фильма: ')

params = {
    'keyword': film_name,
}

headers = {
    'X-API-KEY': api_key,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    film_info = response.json()
    print(film_info)
else:
    print('Ошибка при обращении к API:', response.status_code)