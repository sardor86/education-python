import random
dict1 = {}

for num in range(1, 101):
    dict1[str(f"num{num}")] = random.randint(1, 100)

numbers = 0
for num in dict1:
    numbers += dict1[num]

print(numbers)
print(numbers/len(dict1))
