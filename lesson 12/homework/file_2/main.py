with open("romeo.txt", "r") as file:
    list1 = []

    for word in file.read().lower().replace(' ', '\n').split():
        if not word in list1:
            list1.append(word)

    print(sorted(list1))


