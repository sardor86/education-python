from typing import List


def len_list(words: list): return [len(i) for i in words]


def MAIN():
    words = input("слова: ").split(", ")

    print(len_list(words))


MAIN()
