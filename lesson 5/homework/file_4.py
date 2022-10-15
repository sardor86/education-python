from time import sleep

num1 = 0
num2 = 1
num3 = None
print(f"{num1}\n{num2}")
while True:
    num3 = num1
    num1 = num2
    num2 += num3
    print(num2)
    sleep(0)
