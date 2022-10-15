user_num = int(input("Введите число: "))

numbers = list(range(1, user_num + 1))

numbers_sum = 0

for num in numbers:
    numbers_sum += 1

print(numbers)
print(numbers_sum)