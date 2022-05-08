# TestRun 3
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Проверяются методы на возможность обработки не верных данных. В ответ на такие данные должен приходить ответ с кодом "400".
# Необходимо запускать после успешного прохождения TestRun 1. Т.к. требуются работающие методы.

from api import PetFriends
from settings import *
import os

pf = PetFriends()

def test_add_new_pet_simple_with_big_name():
    """Проверяем что нельзя добавлять питомца с очень длинным именем (big_data). Статус должен быть 400"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, big_data, add_smpl_animal_type, add_smpl_age)

    # удаляем тестовые данные при необходимости
    if type(result) is dict:
        pf.delete_pet(auth_key, result['id'])

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_simple_with_big_animal_type():
    """Проверяем что нельзя добавлять питомца с очень длинной породой (big_data). Статус должен быть 400"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, add_smpl_name, big_data, add_smpl_age)

    # удаляем тестовые данные при необходимости
    if type(result) is dict:
        pf.delete_pet(auth_key, result['id'])

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_simple_with_big_age():
    """Проверяем что нельзя добавлять питомца с очень длинным возрастом (big_data). Статус должен быть 400"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    # status_age, result = pf.add_new_pet_simple(auth_key, add_smpl_name, add_smpl_animal_type, big_data)

    status, result = pf.add_new_pet_simple(auth_key, add_smpl_name, add_smpl_animal_type, big_data)

    # удаляем тестовые данные при необходимости
    if type(result) is dict:
        pf.delete_pet(auth_key, result['id'])

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_with_invalid_photo():
    """Проверяем что нельзя добавить питомца, если в качестве файла выбрано не изображение. Статус должен быть 400"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo_invalid)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, _ = pf.add_new_pet(auth_key, add_name, add_animal_type, add_age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_pet_photo_foreign_user():
    """Проверяем невозможность добавления фото к карточке, если в качестве файла выбрано не изображение. Статус должен быть 400"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo_invalid)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Сначала создадим тестового питомца.
    _, tmp_pet = pf.add_new_pet_simple(auth_key, tmp_name, tmp_animal_type, tmp_age)

    # пробуем изменить с неправильным файлом
    status, res = pf.add_pet_photo(auth_key, tmp_pet['id'], pet_photo)

    # Удаляем временные данные
    pf.delete_pet(auth_key, tmp_pet['id'])

    # Проверяем что статус 400
    assert status == 400