import sqlite3
import random
import time
import datetime

con = sqlite3.connect("demo.db")
cursor=con.cursor()

def addTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")

def randomValue():
    zaman=time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime="Deneme"
    deger=random.randrange(0,10)

    cursor.execute("INSERT INTO Tablo (zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

addTable()

i=0
while (i<10):
    randomValue()
    time.sleep(1)
    i += 1
con.close()



