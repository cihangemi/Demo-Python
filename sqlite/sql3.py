import sqlite3

con = sqlite3.connect("demo.db")
cursor = con.cursor()

def select():
    cursor.execute("SELECT * FROM Tablo where deger = 1.0")
    data=cursor.fetchall()
    for i in data:
        print(i)

select()
con.close()
