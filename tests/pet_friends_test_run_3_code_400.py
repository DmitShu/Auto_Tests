# TestRun 3
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Проверяются методы на возможность обработки не верных данных. В ответ на такие данные должен приходить ответ с кодом "400".
# Необходимо запускать после успешного прохождения TestRun 1. Т.к. требуются работающие методы.

from api import PetFriends
from settings import *
import os

pf = PetFriends()

def test_add_new_pet_simple_with_big_name():
    """Проверяем что нельзя добавлять питомца с очень длинным именем (big_data)"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status_name, result = pf.add_new_pet_simple(auth_key, big_data, add_smpl_animal_type, add_smpl_age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status_name == 400


def test_add_new_pet_simple_with_big_animal_type():
    """Проверяем что нельзя добавлять питомца с очень длинной породой (big_data)"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status_animal_type, result = pf.add_new_pet_simple(auth_key, add_smpl_name, big_data, add_smpl_age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status_animal_type == 400


def test_add_new_pet_simple_with_big_age():
    """Проверяем что нельзя добавлять питомца с очень длинным возрастом (big_data)"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status_age, result = pf.add_new_pet_simple(auth_key, add_smpl_name, add_animal_type, big_data)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status_age == 400