import sqlite3
con =sqlite3.connect("demo.db")
cursor=con.cursor()

def add():
    cursor.execute("CREATE TABLE IF NOT EXISTS info (Name TEXT,Surname TEXT, Age INT)")
def addValue():
    cursor.execute("INSERT INTO info VALUES('Ganxhan','Ozturk','18') ")
    con.commit()
    con.close()

add()
addValue()