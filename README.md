# Автотесты для PetFriends API.

api.py - библиотека к REST api сервису веб приложения Pet Friends (доступные методы описаны здесь https://petfriends1.herokuapp.com/apidocs/#/)
Библиотека api написана в классе, что соответствует принципам ООП и позволяет удобно пользоваться её методами.
Методы имеют подробное описание.

settings.py - сюда вынесены тестовые данные.

/tests - здесь располагается файлы с тестами. Тесты проверяют работу методов используя api библиотеку:

- pet_friends_test_run_1_code_200
Набор тестов для проверки доступных запросов с валидными данными. Каждый тест должен заканчиваться успешным отправлением/получением запросов с возвращением кода "200"

- pet_friends_test_run_2_code_403
Набор тестов для проверки доступных запросов с валидными данными, но не верным ключом аутентификации. Каждый тест должен заканчиваться возвращением кода "403", данные не изменяются/не запрашиваются

- pet_friends_test_run_3_code_400
Набор тестов для проверки доступных запросов с "плохими" данными. Каждый тест должен заканчиваться возвращением кода "400".

- pet_friends_test_run_4_foreign_pets
Набор тестов для проверки невозможности удаления / редактирования карточек, созданных другими пользователями.

/tests/images - здесь находятся файлы, используемые в тестах.




