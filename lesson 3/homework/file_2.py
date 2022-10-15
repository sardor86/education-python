data = []

while True:
    make = None
    try:
        make = int(input("ввдеите действие\n\t1: добавить\n\t2: удалить\n\t3: Посмотреть все данные\nВыбор:"))
        if not 0 < make <= 3:
            print("Вы неправильно вели число")
            input()
            quit()
    except:
        print("Вы неправильно вели число")

    if make == 1:
        name = input("Введите своё имя: ")
        firstname = input("Введите свою фамилию: ")
        old = input("Введите свой возраст: ")

        data.append([name, firstname, old])
        print(f"Ваш индекс {len(data) - 1}\n{name}\n{firstname}\n{old}")

    if make == 2:
        index = int(input("Введите ваш индекс: "))
        data.pop(index)
        print("Удален")
    if make == 3:
        for index, data in list(enumerate(data)):
            print(f"Индекс {index}\n"
                  f"\tИмя {data[0]}\n"
                  f"\tФамилия {data[1]}\n"
                  f"\tВозраст {data[2]}\n"
                  f"##############################################")

    if input("Вы хотите продолжить y/n: ") == "n":
        quit()
    else:
        print("\n\n/////////////////////////////////////////////////////\n\n")
