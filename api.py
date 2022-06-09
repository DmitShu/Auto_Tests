import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from log import logrequests

class PetFriends:
    """апи библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    # GET /api/key This method allows to get API key which should be used for other API methods.
    @logrequests
    def get_api_key(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # GET /api/pets This method allows to get the list of pets.
    @logrequests
    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # POST /api/pets This method allows to add information about new pet.
    @logrequests
    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # DELETE /api/pets/{pet_id} This method allows to delete information about pet from database.
    @logrequests
    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # PUT /api/pets/{pet_id} This method allows to update information about pet.
    @logrequests
    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # POST /api/create_pet_simple This method allows to add information about new pet without photo.
    @logrequests
    def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str,
                    age: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце (без фото) и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    # POST /api/pets/set_photo/{pet_id} This method allows to add photo of a pet.
    @logrequests
    def add_pet_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер фото питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
                   })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


class PetStore:
    """апи библиотека к PetStore"""

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2/"

    # GET /pet/findByStatus/ Finds Pets by status
    @logrequests
    def get_findByStatus(self, stfil: str) -> json:
        """Метод возвращает список по статусу"""

        stfilter = {'status': stfil}

        res = requests.get(self.base_url+'pet/findByStatus', params=stfilter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    # POST /pet Add a new pet to the store.
    @logrequests
    def add_new_pet(self, name: str, status: str = 'available',
                    name_category: str = '', name_tag: str = '',
                    accept: str = 'application/json', content: str = 'application/json') -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце (без фото) и возвращает статус
        запроса на сервер и результат с данными добавленного питомца"""

        headers = {'accept': accept, 'Content-Type':content}

        if content == 'application/json':
            data = {
                    "id": 0,
                    "category": {
                        "id": 0,
                        "name": name_category
                    },
                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": name_tag
                        }
                    ],
                    "status": status
            }
            res = requests.post(self.base_url + 'pet', json=data, headers=headers)
        else:
            data = f"""<?xml version="1.0" encoding="UTF-8"?>
                        <Pet>
                            <id>0</id>
                            <Category>
                                <id>0</id>
                                <name>{name_category}</name>
                            </Category>
                            <name>{name.encode('utf-8')}</name>
                            <photoUrls>
                                <photoUrl>string</photoUrl>
                            </photoUrls>
                            <tags>
                                <Tag>
                                    <id>0</id>
                                    <name>{name_tag}</name>
                                </Tag>
                            </tags>
                            <status>available</status>
                        </Pet>"""
            res = requests.post(self.base_url + 'pet', data=data, headers=headers)

        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    @logrequests
    def add_new_pet_xml(self) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце (без фото) и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = """<?xml version="1.0" encoding="UTF-8"?>
<Pet>
	<id>0</id>
	<Category>
		<id>0</id>
		<name>string</name>
	</Category>
	<name>doggie</name>
	<photoUrls>
		<photoUrl>string</photoUrl>
	</photoUrls>
	<tags>
		<Tag>
			<id>0</id>
			<name>string</name>
		</Tag>
	</tags>
	<status>available</status>
</Pet>"""
        headers = {'accept': 'application/xml', 'Content-Type':'application/xml'}

        res = requests.post(self.base_url + 'pet', data=data, headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
