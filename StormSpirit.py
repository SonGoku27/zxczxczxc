import sqlite3


def star_justice(*data, time=0):
    dbase = sqlite3.connect("bank.sqlite")
    cur = dbase.cursor()
    for place in data:
        sell = cur.execute(f"""""", (place,)).fetchall()
    sell.sort(key=lambda x: x[2], reverse=True)
    return sell


data = ['Baghdad', 'Bursa']
print(*star_justice(*data, time=1), sep='\n')
