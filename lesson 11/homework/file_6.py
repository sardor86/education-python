def fusion_of_list(list1: list[str], list2: list[str]): return [word1 + word2 for word1, word2 in zip(list1, list2)]


def MAIN():
    list1 = input("list1: ").split(", ")
    list2 = input("list2: ").split(", ")

    print(fusion_of_list(list1, list2))


MAIN()
