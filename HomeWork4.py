"""Задание 2"""
import datetime as dt
import requests

def currency_rates(fix_currenc="", url ="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (fix_currenc and url):
        return None

    #Делаем фиксированный регистр
    fix_currenc = fix_currenc.upper()

    response = requests.get(url)

    if response.ok:
        course = response.text.split(fix_currenc)

        #Елси валюты не найдено

        if len(course) == 1:
            return None

        value = course[1].split("</Value>")[0].split("<Value>")[1]
        value = float((value.replace(",", ".")))

        date = response.headers["Date"]
        date = dt.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()

        print(value, date)
    else:
        return None
if __name__ == "__main__":
    print(currency_rates("Usd"))
    print(currency_rates("Eur"))



