money = int(input("Введите количество денег: "))
year = int(input("Введите кодичество лет: "))

result = money

for _ in range(1, year + 1):
    result += money / 100 * 10 + money

print(f"Сумма равна {result}")