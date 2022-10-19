from time import time


def genarated_numbers(number: int): return list(range(number + 1))


def MAIN():
    number = int(input("number: "))
    started = time()
    numbers = genarated_numbers(number)
    end = time()
    print(f"size = {len(numbers)}\n"
          f"time = {end - started}")


MAIN()
