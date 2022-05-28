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