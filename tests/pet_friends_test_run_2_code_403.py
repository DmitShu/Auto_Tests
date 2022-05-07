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
    assert "This user wasn't found in database" in result

def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если email верный, а пароль нет"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    # возможно ответ должен быть другим. Уточнить. Но пока так.
    assert status == 403
    assert "This user wasn't found in database" in result


def test_get_all_pets_with_invalid_key():
    """ Проверяем что запрос всех питомцев возвращает сообщение, а не список питомцев.
    И код ошибки 403
    Доступное значение параметра filter - 'my_pets' либо '' """

    status, result = pf.get_list_of_pets(invalid_key1, '')

    assert status == 403
    assert "Please provide 'auth_key'" in result

def test_add_new_pet_with_invalid_key(name=add_name, animal_type=add_animal_type,
                                     age=add_age, pet_photo=add_pet_photo, auth_key=invalid_key1):
    """Проверяем что добавить питомца с корректными данными из settings.py и неверным ключем нельзя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "Please provide 'auth_key'" in result

def test_delete_pet_with_invalid_key():
    """Проверяем что нельзя удалить питомца с неверным ключем"""

    # Сначала создадим питомца, чтобы случайно не удалить чужого.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pf.add_new_pet(auth_key, tmp_name, tmp_animal_type, tmp_age, tmp_pet_photo)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление с неверным ключем
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(invalid_key1, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 403 и в списке питомцев есть id питомца
    assert status == 403
    assert str(pet_id) in str(my_pets['pets'])
    # Удаляем созданного питомца.
    pf.delete_pet(auth_key, pet_id)

def test_add_new_pet_simple_with_invalid_key(name=add_smpl_name, animal_type=add_smpl_animal_type,
                                     age=add_smpl_age, auth_key=invalid_key1):
    """Проверяем что добавить питомца с корректными данными из settings.py и неверным ключем нельзя"""

    # Пробуем лобавить питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "Please provide 'auth_key'" in result

