def upperName(name: str): return name.title()


def MAIN():
    name = input("names: ").split(", ")

    print(list(map(upperName, name)))
    print(list(map(lambda name2: name2.title(), name)))


MAIN()


