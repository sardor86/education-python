from random import randint

num_list = [randint(1, 1000) for _ in range(1000)]

for number in num_list:
    if number > 500:
        break
    elif number % 5 == 0 and number > 150:
        print(number)