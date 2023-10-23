#Потёмкин Александр 9-ая когорта. Финальный проект. Инженер по тестированию плюс

import configuration
import data
import requests

def post_new_order(body): #создание нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                         json=body)
track = post_new_order(data.new_orders).json()['track'] #получение номера заказа
url = configuration.URL_SERVICE + configuration.TRACK_ORDERS + str(track)
def get_track_order(number): #получение заказа по номеру
   return requests.get(number)
response = get_track_order(url)
def test_status_code(code): #проверка успешного создания заказа
    if code == 200:
        print("Тест пройден")
    else:
        print("Тест провален")
test = test_status_code(response.status_code)