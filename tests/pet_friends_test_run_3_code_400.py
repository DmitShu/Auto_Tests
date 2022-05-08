# TestRun 3
# Блок тестов для описанных методов PetFriends API v1 (https://petfriends1.herokuapp.com/apidocs/#/)
# Проверяются методы на возможность обработки не верных данных. В ответ на такие данные должен приходить ответ с кодом "400".
# Необходимо запускать после успешного прохождения TestRun 1. Т.к. требуются работающие методы.

from api import PetFriends
from settings import *
import os
