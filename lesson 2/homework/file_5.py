year = int(input("Введите год: "))

if not year % 100 == 0 or not year % 400:
    if year % 4:
        print("Этот год высокосный")
else:
    print("Этот год не высокосный")