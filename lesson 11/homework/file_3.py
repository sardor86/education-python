def MAIN():
    words = input("слова: ").split(", ")

    print(list(filter(lambda word: word.lower() == word.lower()[::-1], words)))


MAIN()

