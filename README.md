# Python-test-task-Project
система использует фреймворк django и имеет несколько конечных точек API. Он используется для идентификации магазинов с указанием соответствующего города, улицы, дома, времени открытия, закрытия и того, открыты они или нет

##Получить все магазины
http://127.0.0.1:8000/shops
#Чтобы добавить новый магазин, разместите объект json, подобный этому.
```
{
    "name":"MSU canteen",
    "house":"1",
    "opening_time":"09:00:00",
    "closing_time":"18:00:00",
    "city":"2",
    "street":"3"
}

```

##получить все города
127.0.0.1/city
returns a a response like this 
```
[
    {
        "id": 1,
        "name": "Ulyanovsk"
    },
    {
        "id": 2,
        "name": "Moscow"
    }
    ]
    ```



##получить все улицы
127.0.0.1/city/street

```
[
    {
        "name": "Rozy",
        "city_name": "Moscow"
    },
    {
        "name": "Na done",
        "city_name": "krasnador"
    },
    {
        "name": "Lubyanka",
        "city_name": "Moscow"
    }
]
```
##Фильтруйте магазины по городу, улице и по тому, открыт ли магазин
http://127.0.0.1:8000/shop/?city=1&street=3&open=1

```
[
    {
        "name": "Media Soft",
        "city_name": "Ulyanovsk",
        "street_name": "Lubyanka",
        "house": "67",
        "opening_time": "06:00:00",
        "closing_time": "20:00:00",
        "isOpen": "открывать"
    },
    {
        "name": "Media Soft",
        "city_name": "Ulyanovsk",
        "street_name": "Lubyanka",
        "house": "67",
        "opening_time": "06:00:00",
        "closing_time": "20:00:00",
        "isOpen": "открывать"
    }
]
```

#Установка системы

Клонируйте код из репозитория github: https://github.com/insookwa/Python-test-task-Project 
, используйте ```pip install -r requirements.txt``` установки всех необходимых пакетов .

#База данных
создайте базу данных с именем mediasoft , чтобы иметь возможность выполнять миграции и настраивать необходимые таблицы с помощью django