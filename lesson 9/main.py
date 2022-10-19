# dict_1 = {'c': 1, 'b': 2, 'a': 32}
# res = []
# for key, value in dict_1.items():
#     res.append((key, value))
# print(sorted(res))
# from typing import Union

# def inner_func():
#     return 200
# def something(some_data):
#     some_data += 20
#     return some_data
# def get_and_save_content():
#     return something(inner_func())
# print(get_and_save_content())
# list_1 = range(100)
# def check_num(num: Union[int, float, bool]): return num >= 20
# print(check_num(True))
# print(list(map(str, list_1)))
# check_num(0, 0)
# print(list(map(lambda num, num2: num >= num2, list_1, list_1[::-1])))
# my_func = lambda num, num2: num >= num2
# print(my_func(20, 30))

# def something(num):
#     if num <= 10:
#         print(num)
#         something(num + 1)
# something(1)
# import time
#
#
# def time_checker(func, num) -> tuple:
#     start = time.time()
#     return time.time() - start, func(num).__sizeof__()
# print(time_checker(lambda trash: list(trash), range(1000000)))