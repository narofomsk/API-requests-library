import requests

api_url = 'https://65f1bef1034bdbecc7639165.mockapi.io/items'

header = {
    'Content-Type': 'application/json'
}

cost = float(input('Введите примерную стоимость кроссовок от 8000 до 15000: '))


data = {
    'price': cost
}

response = requests.post(api_url, headers=header, json=data)

if response.status_code == 201:
    shoe = response.json()
    print('Название кроссовок:', shoe['name'])
else:
    print('Ошибка при отправке запроса:', response.status_code)