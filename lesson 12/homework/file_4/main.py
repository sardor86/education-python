def longest_words(file):
    list1 = []
    word = ""
    string = file.read().replace(" ", "\n").split()

    for i in string:
        if len(word) <= len(i):
            word = i

    for i in string:
        if len(word) == len(i):
            list1.append(i)

    return list1
