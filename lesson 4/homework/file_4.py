import random

numbers = [random.randint(1, 1000) for _ in range(1000)]

for num in numbers:
    if num == 815:
        break
    elif num % 2 == 0:
        print(num)