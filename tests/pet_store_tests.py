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


def test_add_new_pet_store(name = "Тест олень", status ='available',
                    name_category = '', name_tag = ''):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Добавляем питомца
    status, result = ps.add_new_pet(name, status, name_category, name_tag)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200