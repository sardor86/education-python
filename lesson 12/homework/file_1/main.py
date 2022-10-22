with open("mbox-short.txt", "r") as file:
    k = 0
    for string in file.read().split("\n"):
        if "From " in string == "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008":
            k = 1
        elif "From " in string:
            k = 0

        if k:
            if "@" in string:
                string1 = string.split(" ")
                for i in string1:
                    if ("@" in i and "." in i) and (not "<" in i):
                        print(i)
