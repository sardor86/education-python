# sum_ = int(input())
# years = int(input())
# for i in range(years):
#     sum_ *= 1.2
# print(int(sum_))

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)


# num_1 = 0
# num_2 = 1
# iteration_count = int(input())
# while iteration_count > 0:
#     new_num_2 = num_1 + num_2
#     num_1 = num_2
#     num_2 = new_num_2
#     print(num_2)
#     iteration_count -= 1

# razmerryada = int(input("Введите размер ряда Фиббоначи: "))
# ryadFibonachi = [0, 1]
# nach = 0
# while nach < razmerryada:
#     num = ryadFibonachi[nach] + ryadFibonachi[nach + 1]
#     ryadFibonachi.append(num)
#     nach += 1
# print("Последовательность Фибоначчи: ", ryadFibonachi)


# dict_1 = {}
# dict_2 = dict()
# print(dict_1)
# print(dict_2)

# a = 1.2
# dict_1 = {
#     "it_center_1": "Tashkent",
#     2: "Andijan",
#     1.1: "dsadsadsa",
#     (1, 2): "Jizzakh",
#     frozenset(): "Bukhara",
#     True: False,
#     False: True,
#     1: "Here new value",
#     (1, 2): "Not Jizzakh",
#     a: 432,
#     "list": [1, 2, 3, 4, 5, {1: 3}],
#     "set": {1, 2, 3, 4, 5},
# }
# print(dict_1[True])
# print(dict_1[1])
# print(dict_1.get(100, "Ключа нет"))
# print(dict_1[(1, 2)])
# dict_1[1] = {"New value": "new value3"}
# print(dict_1)
# dict_1[10000] = 2000
# print(dict_1)
# dict_1.update({1: 2, 3: 4})
# print(dict_1)
# dict_2 = {1: 2}
# dict_3 = {3: 4}
# dict_3 = dict_2 | dict_3 | dict_1 | dict_3
# print(dict_3)
# print(dict_1[1000])
# del dict_1[1]
# print(dict_1)
# dict_1.pop(0)
# print(dict_1.keys())
# print(dict_1.items())
# print(dict_1.values())
# for i in dict_1:
#     print(i, dict_1[i])

# for i in dict_1.keys():
#     print(i, dict_1[i])

# for key, value in dict_1.items():
#     print(key, value)
#     (key, value), (key2, value2)
# if 1 in dict_1:
#     dict_1.pop(1)
#     print("xana")
# for i in dict_1:
#     print(i)

# print(list(enumerate([1, 2, 3, 4])))
# list_1 = list(range(1, 11))
# list_2 = list(range(11, 21))
# print(list_1)
# print(list_2)
# print(dict(zip(list_1, list_2)))

# dict_1.copy()
# dict_1.clear()

# set_1 = set([1, 2, 3, 4, 5, 9])
# set_1.add(2)
# set_1.add(3)
# set_1.add(4)
# set_1.add(5)
# set_1.add(6)
# set_1.add(7)
# set_1.add(-7)
# set_1.add(1)
# set_1.pop()
# print(set_1)
# if 1 in set_1:
#     print("ДА! ОНО ЕСТЬ!!!")

# dict_1 = {
#     "id": 1,
#     "email": "something@gmail.com",
#     "first_name": "Someone",
#     "friends_list": [
#         {
#             "id": 32,
#             "email": "something100@gmail.com",
#             "first_name": "Someone",
#         },
#         {
#             "id": 33,
#             "email": "something2@gmail.com",
#             "first_name": "Someone2",
#         },
#         {
#             "id": 34,
#             "email": "something23@gmail.com",
#             "first_name": "Someone23",
#         }
#     ]
# }
# # email:
# print("email негодника", dict_1['email'])
# print("имя негодника", dict_1['first_name'])
# print("Список собутыльников:")
# for friend in dict_1["friends_list"]:
#     print("\temail:", friend["email"])
#     print("\tимя: ", friend["first_name"])

# 5
# {1: 1, 2: 4, 3: 9}
# moscow, london, tashkent (x, y)
# products = {
#     "lamp": 13143,
#     "cars": 3243242
# }
#
# store = {
#     13143: [
#         {
#             "id": 32,
#             "name": "типа норм лампа",
#             "price": 100000,
#             "quantity": 100
#         },
#         {
#             "id": 33,
#             "name": "типа норм лампа",
#             "price": 100000,
#             "quantity": 100
#         },
#     ],
#     3243242: [
#         {
#             "id": 32,
#             "name": "типа норм лампа",
#             "price": 100000,
#             "quantity": 100
#         },
#         {
#             "id": 33,
#             "name": "типа норм лампа",
#             "price": 100000,
#             "quantity": 100
#         },
#     ]
# }