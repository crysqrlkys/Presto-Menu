# Presto Menu
Design a RESTful web service API call that will return list of items for the restaraunt

# Reasoning
## Why django
Django is a web framework in python. I chose it because of:  

1. Admin Interface (To provide CRUD operations)
2. Testing Framework
3. ORM
4. Reusable django apps and packages 

## Frameworks and packages
1. DRF - fast and convinient way to start your API
2. drf-nested-routers - to create flexible routs 

## Installation
1. Clone repository
2. Create empty postgresql database named `presto`
3. Create virtual environment `python3 -m venv venv`
4. Activate venv by `source venv/bin/activate`
5. Install packages `pip install -r requirements.txt`
6. Migrate `./manage.py migrate`
7. Create super user `./manage.py createsuperuser`
8. Run server `./manage.py runserver`

## How to use
Database is empty by default so you should add some instances through django admin web interface  
All methods provided by API are read-only  
```
GET /restaurants/  
GET /restaurants/<id>/  
GET /restaurants/<id>/item
```

## Response examples

GET /restaurants/
```json
[
    {
        "id": 1,
        "title": "KFC",
        "address": "somewhere"
    },
    {
        "id": 2,
        "title": "Burger King",
        "address": "anywhere"
    }
]
```
GET /restaurants/1/item/
```json
[
    {
        "id": 1,
        "title": "Burger",
        "cost": 20,
        "modifiers": [
            {
                "id": 1,
                "title": "Sauce",
                "parent": null,
                "children": [
                    {
                        "id": 3,
                        "title": "Curry",
                        "parent": 1,
                        "children": []
                    },
                    {
                        "id": 4,
                        "title": "Ketchup",
                        "parent": 1,
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "id": 2,
        "title": "Drink",
        "cost": 15,
        "modifiers": [
            {
                "id": 2,
                "title": "Ice",
                "parent": null,
                "children": []
            }
        ]
    }
]
```