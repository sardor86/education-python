import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

dict1 = {}

for lis1, lis2 in zip(list1, list2):
    dict1[lis1] = lis2

print(dict1)
