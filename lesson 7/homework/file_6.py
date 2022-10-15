def upper_in_string(strings):
    numbers = 0
    for string in strings:
        if string.isupper():
            numbers += 1

    return numbers


def lower_in_string(strings):
    numbers = 0
    for string in strings:
        if string.islower():
            numbers += 1

    return numbers
