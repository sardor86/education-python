# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# print(BASE_DIR)

# import os

# if not os.path.exists("inner_file"):
#    os.mkdir("inner_file")
# os.rmdir("inner_file")

# w/wb
# w+
# r/rb
# r+
# a

# opened_file = open("../config.txt", "w", encoding="utf-8")
# opened_file.write("sasAssaSASAsAdassadas")
#
# opened_file.close()

opened_file = open("../config.txt", "a")

while True:
    opened_file.write("\tHACKED\n")

