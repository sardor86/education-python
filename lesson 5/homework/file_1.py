products_list = []
while True:
    command = input("Введите команду\n"
                    "add: Добавить продукт в корзину\n"
                    "delete: Удалить продукт с корзиныn\n"
                    "list: Список продуктов\n"
                    "search: Искать продукт\n"
                    "clear: Очистить корзину\n"
                    "stop: Остановить программу\n"
                    "Ввод: ").lower()
    if command == "list":
        if not products_list:
            print("Продуктов нет)))")
            continue
        print(", ".join(products_list))
    elif command == "add":
        product_name = input("Введите название продукта: ")
        if product_name in products_list:
            print("Продукт уже существует)))")
            continue
        products_list.append(product_name)
        print("Добавил успешно!")
    elif command == "delete":
        product_name = input("Введите название продукта: ")
        if product_name not in products_list:
            print("Продукт не существует)))")
            continue
        products_list.remove(product_name)
        print("Удалил успешно!")
    elif command == "search":
        product_name = input("Введите название продукта: ")
        if product_name in products_list:
            print("Такой продукт существует в корзине")
        else:
            print("Такого продукта не существует в корзине")
    elif command == "clear":
        products_list.clear()
    elif command == "stop":
        break
    else:
        print("Какой же ты дурачок))")