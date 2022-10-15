def sum_number(number):
    number = str(number)
    result = 0

    for num in number:
        result += int(num)

    return result
