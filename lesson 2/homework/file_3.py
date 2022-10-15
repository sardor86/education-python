num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

Coincidence = 0

if num_1 == num_2:
    if Coincidence == 0:
        Coincidence += 2
    else:
        Coincidence += 1
if num_1 == num_3:
    if Coincidence == 0:
        Coincidence += 2
    else:
        Coincidence += 1
if num_2 == num_3:
    if Coincidence == 0:
        Coincidence += 2
    else:
        Coincidence += 1

print(f"Совпадаемых чисел {Coincidence}")