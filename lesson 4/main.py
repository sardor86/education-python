# list_1 = [1, 5, 3483, 543, 54, 5, 4, 1, 2]
# list_2 = []
# list_3 = []
# for i in list_1:
#     if i <= 5: list_2.append(i)
#     else: list_3.append(i)
# print(list_2)
# print(list_3)
# from random import randint

# list_1 = []
# name, surname, age = input().split()
# list_1.append([name, surname, age])
# print(list_1)

# nums_list = input().split(", ")
# print(nums_list)

# nums = input().split("+")
# sum_ = 0
# for i in nums:
#     sum_ = sum_ + int(i)
# print(sum_)
# print(eval(input()))

# list_1 = [1, 2, 3, 4, 4, 5]
# # list_2 = []
# # for i in list_1:
# #     list_2.append(i ** 2)
# # print(list_2)

# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]
# print(list_1 == list_2)
# print(list_1 is list_2)
# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3
# print(tuple_1 == tuple_2)
# print(tuple_2 is tuple_1)
# int1 = 300
# int2 = 300
# print(int1 == int2)
# print(int1 is int2)
# list_1.clear()
# print(list_1)
# list_1.extend((1, 2, 3))
# print(list_1)
# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3
# tuple_3 = tuple([1, 2, 3])
# print(tuple_1 is tuple_3)
# print(tuple_2)
# print(tuple_3)
# str_1 = "dasdsasad"
# str_3 = "dasdsasad"
# str_2 = str([1, 2, 3])
# print(str_1 is str_3)
# print(str_2)
# print(str_1.upper())
# print(str_1.lower())
# print(str_1.capitalize())
# print(str_1.title())
# print(str_1.index())
# print(str_1.count())

# range(10)
# range(10, 20)
# range(10, 20, 3)

# list_2 = [i ** 2 for i in list_1 if i > 2]
# print(list_2)
# list_2 = (i ** 2 for i in list_1)
# print(list(list_2))
# print([i for i in list_2])
# print(10 if 20 > 10 and 20 > 30 else 30)

# list_1 = []
# for i in range(100):
#     if i % 2 == 0:
#         list_1.append(i)
# print(list_1)
# print([i for i in range(100) if i % 2 == 0])
# print(list(range(0, 100, 2)))

# list_1 = str(randint(1, 100) for _ in range(10))
# print(list_1)
# print(min(list_1))
# print(max(list_1))
# print(sum([1, 2, 4, 5]))

# list_1 = [1, 2, 3, 4, 5]
# start:end:step
# print(list_1[1:])
# print(list_1[:4:])
# print(list_1[::])
# print(list_1[::-1])
# print(list_1)

# list_1 = [1, 2, 3, 4, 5]
# list_2 = list_1 + [1, 2]
# # list_2.append(19)
# print(id(list_1))
# print(id(list_2))
# print(list_1)
# print(list_2)
# for i in range(1, 10):
#     if i % 2 == 0:
#         print("Троян найден!")
#         break
# else:
#     print("SUCCESS")
#
# data = [input(), input(), input()]
# print(data)

# data = [
#     input("Введите ваш возраст: "),
#     input("боlел ли ты короновирусом: ").lower(),
#     input("Введите ваш рост: ")
# ]
#
# for i in data:
#     if i.isdigit():
#         if 18 > int(i) < 160:
#             print("НЕГОДЕН!!!")
#             break
#     if i == "да":
#         print("НЕГОДЕН!!!")
#         break
# else:
#     print("Ты годен!(к сожадению) Плати 550$")

