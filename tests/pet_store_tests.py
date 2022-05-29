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
    """Время выполнения не более 1 с"""
    assert time_del.total_seconds() < 1

def generate_string(n):
   return "x" * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


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


@pytest.mark.parametrize("filter", [generate_string(255),
                                    generate_string(1001),
                                    russian_chars(),
                                    chinese_chars(),
                                    special_chars(),
                                    123,
                                    ],
                         ids= ['255 symb',
                               '1001 symb',
                               'russian',
                                'chinese',
                                'special',
                                '123'
                               ])
def test_get_findByStatus_negative(filter):

   pytest.status, result = ps.get_findByStatus(filter)
   """Проверяется /pet/findByStatus/ c неверными значениями фильтра"""

   assert 'id' and 'category' and 'name' and 'photoUrls' not in str(result)
   assert pytest.status == 200

@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
def test_add_new_pet_store(name, status ='available',
                    name_category = '', name_tag = ''):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Добавляем питомца
    status, result = ps.add_new_pet(name, status, name_category, name_tag)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    assert result['status'] == status

# def is_age_valid(age):
#    # Проверяем, что возраст - это число от 1 до 49 и целое
#    return age.isdigit() \
#           and 0 < int(age) < 50 \
#           and float(age) == int(age)
#
#
# @pytest.mark.parametrize("name"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("animal_type"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("age"
#    , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
#    , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])