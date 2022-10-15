import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(0, 10))

list1 = []
list2 = []
for num in numbers:
    if num <= 5:
        list1.append(num)
    else:
        list2.append(num)

print(numbers)
print(list1)
print(list2)
