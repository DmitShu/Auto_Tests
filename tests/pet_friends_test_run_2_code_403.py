# TestRun 2
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Заданы валидные данные, но логин / пароль / auth_key не существующие. ОР: везде статус должен быть 403.

from api import PetFriends
from settings import *
import os

pf = PetFriends()

def test_get_api_key_for_invalid_mail(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если email не верный"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если email верный, а пароль нет"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_invalid_key():
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    status, result = pf.get_list_of_pets(invalid_key1, '')

    assert status == 403
    assert "Please provide 'auth_key'" in result