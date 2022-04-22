"""Задание 4"""

import sys

import HomeWork4

args = sys.argv[1:]

for code in args:
    conv = HomeWork4.currency_rates(code)
    if conv:
        cur, date = conv
        date = date.strftime("%d-%m-%Y")
        print(f"{cur}, {date}")