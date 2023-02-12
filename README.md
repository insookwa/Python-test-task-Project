# Python-test-task-Project
система использует фреймворк django и имеет несколько конечных точек API. Он используется для идентификации магазинов с указанием соответствующего города, улицы, дома, времени открытия, закрытия и того, открыты они или нет


##Получить все магазины
http://127.0.0.1:8000/shops
![Screenshot from 2023-02-12 12-34-51](https://user-images.githubusercontent.com/42169195/218313748-2c4e1bbc-d7fa-4183-acba-9fc755fd9648.png)



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
![Screenshot from 2023-02-12 13-23-47](https://user-images.githubusercontent.com/42169195/218313502-9524a758-41bd-4549-9c78-3603227f580e.png)

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

![Screenshot from 2023-02-12 12-35-22](https://user-images.githubusercontent.com/42169195/218313667-01d984a6-ec37-45ce-acec-eef7b3ad30b5.png)


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
![Screenshot from 2023-02-12 12-51-19](https://user-images.githubusercontent.com/42169195/218313565-0eb545ed-feba-450f-931d-b8e092354b4b.png)
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
![Screenshot from 2023-02-12 15-09-38](https://user-images.githubusercontent.com/42169195/218313627-a4bca304-73ad-4f87-b6cd-ec3e36e7eff8.png)



#Установка системы

Клонируйте код из репозитория github: https://github.com/insookwa/Python-test-task-Project 
, используйте  ```pip install -r requirements.txt```установки всех необходимых пакетов .

#База данных
создайте базу данных с именем mediasoft , чтобы иметь возможность выполнять миграции и настраивать необходимые таблицы с помощью django
