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
    # Удаляем временные данные.
    pf.delete_pet(auth_key_1, pet_id)

    # Проверяем что статус ответа равен 403 и в списке питомцев есть id питомца
    assert status == 403
    assert str(pet_id) in str(my_pets['pets'])
