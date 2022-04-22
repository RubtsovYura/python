"""Задание 1"""

def pars(file = "pars.txt"):
    if file:
        with open(file, 'r', encoding= "utf-8") as f:
            for line in f:
                ip = line.split("- -")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield (ip, rsp, pth)
def spam(file = 'pars.txt'):

    parsed = pars(file)
    db = {}

    for log in parsed:
        db[log[0]] = db.get(log[0], 0) + 1
    return max(db.items(), key=lambda x: x[1])
if __name__ == "__main__":
    parsed = pars()

    for el in range(5):
        print(next(parsed))

    spamer = spam()
    if spamer:
        print(f"ip spamer: {spamer[0]}, count: {spamer[1]}")

"""Задание 3"""
import json
from mod import generator

def group(
        user_pth="users.csv",
        hobby_pth="hobby.csv"):

    if not (user_pth or hobby_pth):
        return -1

    user_lines = None
    hobby_lines = None

    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1
    print(hobby_lines)
    print(user_lines)

    groups = {}

    for fio, hobby in generator(user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        groups[fio] = hobby.replace("\n", "") if hobby else None

    with open("out.txt", "a", encoding="utf-8") as out_file:
        out_file.writelines(json.dumps(groups))
    print(groups)

    return 0