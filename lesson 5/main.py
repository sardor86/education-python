# list_1 = ['pizza', 'пельмени']
# list_2 = list_1.copy()
# list_2.append('плов')
# print(list_1)
# print(list_2)

# user_num = int(input())
# print(list(range(1, user_num+1)))
# print(sum(range(1, user_num+1)))


# list_1 = list(range(1, 100, 2))
# list_2 = list(range(0, 100, 2))
# print(list_1)
# print(list_2)
# print(sum(list_1))
# print(sum(list_2))


# list_1 = [1, 2, 6, 815, 321, 543, 67, 43]
# for i in list_1:
#     if i == 816:
#         break
#     elif i % 2 == 0:
#         print(i)

# print(len(input()))

# end = int(input())
# for num in range(2, end+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)
# from random import randint
#
# list_1 = [randint(1, 9) for _ in range(20)]
# print(list_1)
# for i in list_1:
#     if i % 2 != 0:
#         continue
#     print(i)

# for i in range(1, 10):
#     for num in range(i):
#         print(num, end="")
#     print()
# from time import sleep
# num = 1
# stop = True
# while stop:
#
#     if num % 2 == 0:
#         print(num)
#         stop = False
#     num += 1
# num += 1
# sleep(.01)


# while True:
#     for i in range(10):
#         print(i, end="")
#     print()


# num = 1
# print(num)
# num += 1
# print(num)
# num = num + 1
# print(num)
# num -= 1
# print(num)
# num = num - 1
# print(num)

# users_list = []
# while True:
#     email = input("email: ")
#     if "@" not in email:
#         print("Балда! Введи норм email")
#         continue
#     elif len(email.split("@")) <= 2 and email.split("@")[-1] in ["", " ", "axaxa"]:
#         print("Хитрая крыса! Научись ввести email")
#         continue
#     emails = [i[0] for i in users_list]
#     if email in emails:
#         print("Ля ты крыса! Тебя уже есть в нашей базе данных")
#         continue
#     password = input("password: ")
#     if len(password) < 6:
#         print("Тупой! Мой младшый брат и то надёжнее пишет!")
#         continue
#     elif password == email:
#         print("Ору...")
#         continue
#     users_list.append([email, password])


# products_list = []
# while True:
#     command = input("Введите команду\n"
#                     "add: Добавить продукт в корзину\n"
#                     "delete: Удалить продукт с корзиныn\n"
#                     "list: Список продуктов\n"
#                     "Ввод: ").lower()
#     if command == "list":
#         if not products_list:
#             print("Продуктов нет)))")
#             continue
#         print(", ".join(products_list))
#     elif command == "add":
#         product_name = input("Введите название продукта: ")
#         if product_name in products_list:
#             print("Продукт уже существует)))")
#             continue
#         products_list.append(product_name)
#         print("Добавил успешно!")
#     elif command == "delete":
#         product_name = input("Введите название продукта: ")
#         if product_name not in products_list:
#             print("Продукт не существует)))")
#             continue
#         products_list.remove(product_name)
#         print("Удалил успешно!")
#     else:
#         print("Какой же ты дурачок))")