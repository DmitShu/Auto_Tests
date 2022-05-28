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
    print (f"\nТест шел: {end_time - start_time}")
    """Будет выполняться перед каждым тестом и измерять время выполнения"""


def test_get_findByStatus(stfil='available'):
    """ Проверяем что запрос возвращает не пустой список"""

    status, result = ps.get_findByStatus(stfil)

    assert status == 200
    assert 'id' and 'category' and 'name' and 'photoUrls' in str(result)


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
                                    'sold',
                                    generate_string(255),
                                    generate_string(1001),
                                    russian_chars(),
                                    chinese_chars(),
                                    special_chars(),
                                    123,
                                    ],
                         ids= ['available',
                               'pending',
                               'sold',
                               '255 symb',
                               '1001 symb',
                               'russian',
                                'chinese',
                                'special',
                                '123'
                               ])
def test_get_findByStatus_all(filter):

   pytest.status, result = ps.get_findByStatus(filter)

   # assert 'id' and 'category' and 'name' and 'photoUrls' in str(result)
   assert pytest.status == 200