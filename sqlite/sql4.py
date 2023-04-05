"""Update abd Delete"""
import sqlite3

con = sqlite3.connect("demo.db")
cursor = con.cursor()

def update():
    cursor.execute("SELECT * FROM Tablo")
    data =cursor.fetchall()
    print("------------ORİJİNAL------------")
    for i in data:
        print(i)
    cursor.execute("UPDATE Tablo SET deger=20 WHERE deger=1")
    cursor.execute("SELECT * FROM Tablo")
    data=cursor.fetchall()
    print("---------------Update--------------")
    for i in data:
        print(i)

def delete():
    cursor.execute("SELECT * FROM Tablo")
    data=cursor.fetchall()
    print("--------------ORİJİNAL-----------------")
    for i in data:
        print(i)
    cursor.execute("DELETE From Tablo where deger=2")
    cursor.execute("SELECT * FROM Tablo")
    data=cursor.execute("SELECT * FROM Tablo")
    print("--------------DELETED---------")
    for i in data:
        print(i)




update()
delete()
con.close()