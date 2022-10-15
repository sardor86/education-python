print("Например 5 + 5 + 3")
num = input("Введите пример со сложением: ")

numbers = num.split(" + ")
numbers = [int(number) for number in numbers]

result = 0
for number in numbers:
    result += number

print(f"Сумма равна {result}")