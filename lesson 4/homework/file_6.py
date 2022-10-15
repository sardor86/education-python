long_numbers = int(input("Введите число: "))

numbers = list(range(long_numbers + 1))

for num1 in numbers:
    for num2 in range(2, num1):
        if num1 % num2 == 0:
            break
    else:
        print(num1)