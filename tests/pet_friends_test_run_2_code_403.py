# TestRun 2
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Заданы валидные данные, но логин / пароль / auth_key не существующие. ОР: везде статус должен быть 403.

from api import PetFriends
from settings import *
import os

pf = PetFriends()