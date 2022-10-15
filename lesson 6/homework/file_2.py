numbers = int(input("Введите число: "))

dict1 = {}

for num in range(1, numbers + 1):
    dict1[num] = num**2

print(dict1)
