####SONA EKLEME####
""""
with open("hector.txt","a") as dosya:
    dosya.write("Pubg: Gold IV")
    otomatik olarak en sona ekleme yapar
"""
####BAŞA EKLEME#####
"""
with open("hector.txt","r+") as dosya:
    data = dosya.read()
    dosya.seek(0)
    data="Dota2: Guardin\n"+data
    dosya.write(data)
    """
### ORTAYA EKLEME ###
"""liste = [1,2,3,4]
liste.insert(1,999)
print(liste)"""

with open("hector.txt","r+") as dosya:
    liste=dosya.readlines()
    liste.insert(2,"Fortnite: Silver\n")
    dosya.seek(0)
    dosya.writelines(liste)


