import random

list_num = []
for num in range(10):
    list_num.append(random.randint(0, 10))

print(list_num)

result_num = []
for num in list_num:
    result_num.append(num**2)

print(result_num)
