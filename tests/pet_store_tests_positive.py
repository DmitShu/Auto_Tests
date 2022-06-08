# PetStore testing
# Тестирование методов для petstore (впеменные)

from datetime import datetime
from api import PetStore
from settings import *
import os
import pytest

ps = PetStore()

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    time_del = end_time - start_time
    print (f"\nТест шел: {time_del}")
    """Время выполнения не более 3 с"""
    assert time_del.total_seconds() < 3

@pytest.mark.parametrize("filter", ['available',
                                    'pending',
                                    'sold'
                                    ],
                         ids= ['available',
                               'pending',
                               'sold'
                               ])
def test_get_findByStatus_positive(filter):

   pytest.status, result = ps.get_findByStatus(filter)
   """Проверяется /pet/findByStatus/ c валидными значениями фильтра"""

   assert 'id' and 'category' and 'name' and 'photoUrls' in str(result)
   assert pytest.status == 200


# @pytest.mark.parametrize("name", [
#    ''
#    , generate_string(255)
#    , generate_string(1001)
#    , russian_chars()
#    , russian_chars().upper()
#    , chinese_chars()
#    , special_chars()
#    , '123'
# ], ids=[
#    'empty'
#    , '255 symbols'
#    , 'more than 1000 symbols'
#    , 'russian'
#    , 'RUSSIAN'
#    , 'chinese'
#    , 'specials'
#    , 'digit'
# ])

# @pytest.mark.parametrize("accept", [
#    'application/json'
#    , 'application/xml'
# ], ids=[
#    'accept json'
#    , 'accept xml'
# ])
# @pytest.mark.parametrize("content", [
#    'application/json'
#    , 'application/xml'
# ], ids=[
#    'content json'
#    , 'content xml'
# ])
def test_add_new_pet_store_positive(accept = 'application/xml', content = 'application/xml', name = 'ЙУХ', filter ='available',
                    name_category = '', name_tag = ''):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Добавляем питомца
    status, result = ps.add_new_pet(name, filter, name_category, name_tag, accept, content)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    # assert result['name'] == name
    # assert result['status'] == filter

# @pytest.mark.parametrize("name"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("animal_type"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("age"
#    , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
#    , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])