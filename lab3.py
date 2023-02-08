import random
import os, os.path

ALPHABET = "qwertyuiopasdfghjklzxcvbnm1234567890_"

def parse_csv() -> dict:
    got_data = {}

    with open("data_3.csv", "r") as raw_csv:
        for line in raw_csv:
            (idx, nick, text, likes) = line.replace("\n", "").split(",")
            got_data.update({int(idx): {"nickname": nick, "text": text, "likes": int(likes)}})

    return got_data

def sorted_by_nickname(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda f: f[1]["nickname"]))

def sorted_by_likes_count(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda f: f[1]["likes"], reverse=True))

def select_rows_with_likes_more_than(d: dict, value: int) -> dict:
    return dict((k, v) for k, v in d.items() if v["likes"] > value)

def add_new_data(d: dict, nick: str, text: str):
    with open("data_3.csv", "w") as f:
        for k, v in d.items():
            f.write(f"{k},{v['nickname']},{v['text']},{v['likes']}\n")
        f.write(f"{list(d.items())[-1][0]+1},{nick},{text},0\n")

def get_files_count_in_directory(path: str):
    (loc, dirs, files) = next(os.walk(path))

    return len(files)


if __name__ == "__main__":
    dir = input("Папка с файлами: ")
    print(f"Количество файлов в папке: {get_files_count_in_directory(dir)}\n\n")

    data = parse_csv()

    sn_data = sorted_by_nickname(data)
    for k, v in sn_data.items():
        print(f"Запись №{k}\nОт кого: {v['nickname']}\nЛайки: {v['likes']}\nТекст: {v['text']}\n")

    print(f'{"".join(["-" for i in range(64)])}\n')

    sl_data = sorted_by_likes_count(data)
    for k, v in sl_data.items():
        print(f"Запись №{k}\nОт кого: {v['nickname']}\nЛайки: {v['likes']}\nТекст: {v['text']}\n")

    print(f'{"".join(["-" for i in range(64)])}\n')

    slc_data = select_rows_with_likes_more_than(data, 500)
    for k, v in slc_data.items():
        print(f"Запись №{k}\nОт кого: {v['nickname']}\nЛайки: {v['likes']}\nТекст: {v['text']}\n")

    add_new_data(data, "".join([random.choice(ALPHABET) for i in range(random.randint(8, 16))]), "".join([random.choice(ALPHABET) for i in range(random.randint(16, 32))]))
