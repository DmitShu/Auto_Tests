# TestRun 4
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Проверяются методы на невозможность изменения / удаления данных чужих пользователей.

from api import PetFriends
from settings import *
import os

pf = PetFriends()

def test_delete_pet_foreign_user():
    """Проверяем невозможность удаления питомца чужого пользователя"""

    # Получаем ключи разных пользователей (зареганы в системе).
    _, auth_key_1 = pf.get_api_key(valid_email, valid_password)
    _, auth_key_2 = pf.get_api_key(valid_email_2, valid_password_2)

    # Создадим тестового питомца пользователя 1.
    _, tmp_pet = pf.add_new_pet_simple(auth_key_1, tmp_name, tmp_animal_type, tmp_age)

    # Берём id  питомца пользователя 1 и отправляем запрос на удаление с ключом пользователя 2
    pet_id = tmp_pet['id']
    status, _ = pf.delete_pet(auth_key_2, pet_id)

    # Ещё раз запрашиваем список питомцев пользователя 1
    _, my_pets = pf.get_list_of_pets(auth_key_1, "my_pets")

    # Удаляем временные данные теста пользователя 1
    pf.delete_pet(auth_key_1, pet_id)

    # Проверяем что в списке питомцев есть id питомца (не удален) и статус ответа не 200.
    assert str(pet_id) in str(my_pets['pets'])
    assert status != 200


def test_update_pet_info_foreign_user():
    """Проверяем невозможность изменения питомца чужого пользователя"""

    # Получаем ключи разных пользователей (зареганы в системе).
    _, auth_key_1 = pf.get_api_key(valid_email, valid_password)
    _, auth_key_2 = pf.get_api_key(valid_email_2, valid_password_2)

    # Сначала создадим питомца пользователя 1, для попытки изменения.
    _, tmp_pet = pf.add_new_pet_simple(auth_key_1, tmp_name, tmp_animal_type, tmp_age)

    # пробуем изменить пользователем 2 и проверяем питомцев пользователя 1
    status, _ = pf.update_pet_info(auth_key_2, tmp_pet['id'], upd_name, upd_animal_type, upd_age)
    _, my_pets = pf.get_list_of_pets(auth_key_1, "my_pets")

    # Удаляем временные данные теста
    pf.delete_pet(auth_key_1, tmp_pet['id'])

    # Проверяем что данные питомца не изменились и статус ответа не 200.
    assert my_pets['pets'][0]['name'] == tmp_name
    assert my_pets['pets'][0]['animal_type'] == tmp_animal_type
    assert my_pets['pets'][0]['age'] == tmp_age
    assert status != 200


def test_add_pet_photo_foreign_user():
    """Проверяем невозможность добавления фото к карточке чужого пользователя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), add_pet_photo3)

    # Получаем ключи разных пользователей (зареганы в системе).
    _, auth_key_1 = pf.get_api_key(valid_email, valid_password)
    _, auth_key_2 = pf.get_api_key(valid_email_2, valid_password_2)

    # Сначала создадим питомца пользователя 1, для попытки изменения.
    _, tmp_pet = pf.add_new_pet_simple(auth_key_1, tmp_name, tmp_animal_type, tmp_age)

    # пробуем изменить пользователем 2 и проверяем питомцев пользователя 1
    status, _ = pf.add_pet_photo(auth_key_2, tmp_pet['id'], pet_photo)
    _, my_pets = pf.get_list_of_pets(auth_key_1, "my_pets")

    # Удаляем временные данные
    pf.delete_pet(auth_key_1, tmp_pet['id'])

    # Проверяем что фото не было изменено и статус не 200
    assert my_pets['pets'][0]['pet_photo'] == ''
    assert status != 200

# def test_tmp_testts():
#     """временный метод для проверок"""
#     _, auth_key_2 = pf.get_api_key(valid_email_2, valid_password_2)
#
#     _, allpets = pf.get_list_of_pets(auth_key_2, "")
#
#     for i in allpets['pets']:
#         stat, res = pf.delete_pet(auth_key_2, i['id'])
#         print(stat)
#         print(res)

