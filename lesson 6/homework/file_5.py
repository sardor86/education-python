cities = {
    'Moscow': (550, 370),
    'london': (510, 510),
    'paris': (480, 480)
}

dict1 = {}

for city in cities:
    for other_city in cities:
        if other_city != city:
            print(cities[other_city][0])
            dict1[f"{city} and {other_city}"] = ((cities[city][0] - cities[other_city][0])**2 + (cities[city][1] - cities[other_city][1])**2) ** 0.05

print(dict1)
