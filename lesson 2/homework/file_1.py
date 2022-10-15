old = int(input("Введите ваш возраст: "))

if old <= 18:
    print("Вам нужно учиться")
elif 18 < old <= 50:
    print("Вам нужно работать")
elif 50 < old <= 60:
    print("Вам скоро на пенсию")
elif 60 < old <= 110:
    print("Вы пенсионер")
else:
    print("БЕСМЕРТНЫЙ ?")