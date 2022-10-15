list1 = list(range(2, 102, 2))
list2 = [num - 1 for num in list1]

list1_sum = 0
list2_sum = 0

for num in list1:
    list1_sum += num

for num in list2:
    list2_sum += num

print(list1)
print(list2)
print(list1_sum)
print(list2_sum)