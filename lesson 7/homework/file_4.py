def perevorot(strings):
    result_str = ""
    for num in range(len(strings)):
        print(len(strings))
        result_str += strings[len(strings) - num - 1]
    return result_str
