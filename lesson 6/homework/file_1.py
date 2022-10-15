goods = {
    'Лампа': 12345,
    'Стол': 23456,
    'Диван': 34567,
    'Стул': 45678
}

store = {
    '12345': [
        {
            'quantity': 27,
            'price': 42
        }
    ],
    '23456': [
        {
            'quantity': 22,
            'price': 42
        }
    ],
    '34567': [
        {
            'quantity': 2,
            'price': 42
        }
    ],
    '45678': [
        {
            'quantity': 50,
            'price': 42
        },
        {
            'quantity': 12,
            'price': 95
        },
        {
            'quantity': 43,
            'price': 97
        }
    ]
}

for name in goods:
    money = 0
    for things in store[str(goods[name])]:
        money = things['quantity'] * things['price']
    print(f"{name} : {money}$")
