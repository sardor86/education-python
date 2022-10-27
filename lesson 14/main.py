from os import getcwd, mkdir
from os.path import exists
import requests


def saveJpgCats(status_code: int) -> int:
    content = requests.get(f"http://http.cat/{status_code}")

    if content.status_code == 200:
        CATS_DIR = getcwd() + "\\CATS_IMG"
        if not exists(CATS_DIR):
            mkdir(CATS_DIR)
        with open(f"{CATS_DIR}\\{status_code}.jpg", "wb") as file:
            file.write(content.content)
        return 200
    else:
        return content.status_code
