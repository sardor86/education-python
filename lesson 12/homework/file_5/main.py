def perevorot(file) -> str: return "\n\n".join(["\n".join([k for k in i.split("\n")][::-1]) for i in file.read().split("\n\n")])


def MAIN():
    with open("Poems.txt", "w") as file:
        file.write(perevorot(open("byron.txt", "r")) + perevorot(open("pushkin.txt", "r")) +
                   perevorot(open("pushkin2.txt", "r")) + perevorot(open("romeo.txt", "r")))


MAIN()
