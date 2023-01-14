string ="hector"
for i in string:
    print(i)

liste = ["Ankara","Antalya","Denizli","Isparta"]
for i in liste:
    print(i)

#range fonksiyonu içine aldığı değerleri kullanarak liste oluşturur.
print(*range(10))
#0,1,2,3,4,5,6,7,8,9
print(*range(2,10))
#2,3,4,5,6,7,8,9
print(*range(10,100,10))
#10,20,30,40,50,60,70,80,90

for i in range(1,10):
    print(i*'*')
"""
*
**
***
****
*****
******
*******
********
*********
"""

