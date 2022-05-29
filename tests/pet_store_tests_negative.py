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