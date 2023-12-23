# Project Description

A small CMD system that allows to register for a set of tables at a restaurant.

At any time, the user can add a dish to a table.

The user can select to "checkout" the table, which should show what is the total ammount to be paid.

When adding a dish to the table, he should be able to select from a pre-defined list of elements.

Table 1..10 # Static

Meniu x elemente # Static



```python
# Masa e compusa din Nume si Lista de comnezi
# Meniul e compus din Nume la bucata si pretul bucatii

table_data = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}

drinks_options = [
    {
        "name": "Coco-Cola",
        "price": 25.0
    },
    {
        "name": "Dorna",
        "price": 10.0
    },
    {
        "name": "Vin Alb/Rosu",
        "price": 40.0
    },
    {
        "name": "Ceai",
        "price": 20.0
    },
    {
        "name": "Cafea Americano/Espresso",
        "price": 20.0
    },
    {
        "name": "Cafea Latte",
        "price": 30.0
    },
]
salads = [
    {"name": "Caesar Salad", "price": 60},
    {"name": "Olivie", "price": 100},
    {"name": "Greek Salad", "price": 60},
    {"name": "Summer Salad", "price": 40},
]
soups = [
    {"name": "Bors Rosu", "price": 50},
    {"name": "Supa Crema", "price": 50},
    {"name": "Supa Taraneasca", "price": 50},
    {"name": "Chicken Noodle soup", "price": 50},
]

main_dishes = [
    dict(name="Cartofi Pai cu Chicken Nuggets", price=50),
    dict(name="Friptura cu Mamaliguta si branza", price=50),
]

menu = {
    'drinks': drinks_options,
    'salads': salads,
    'soups': soups,
    'main': main_dishes
}

```
