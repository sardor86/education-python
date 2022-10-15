pupil = int(input("Введите количество учеников: "))
apple = int(input("Введите количество яблок в корзине: "))

print(f"Каждому ученику достаётся {apple // pupil}")
print(f"В корзине остается {apple % pupil}")