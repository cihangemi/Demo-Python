

import calc
#2. import yöntemi
# 'from calc import * calc' den bütün fonksiyonları alır
# fonksiyon çağırırken sadece fonksiyon yazmak yeterli
# örn topla()#

print("Calculator v0.001")
print("+:Toplama\n-:Çıkarma\n/:Bölme\n*:Çarpma")

while(True):
    n1 = int(input("1.sayi:"))
    n2 = int(input("2.sayi:"))
    choose=input("Yapmak istediğiniz işlemi yukarıda belirtilen şekilde seiçiniz:")

    if choose == '+':
        calc.topla(n1,n2)
    elif choose == '-':
        calc.cikar(n1,n2)
    elif choose == '/':
        calc.bol(n1,n2)
    elif choose == '*':
        calc.carp(n1,n2)
    else:
        print("Hatalı giriş\nTekrar girin")
    onay = input("Devam etmek İster misiniz ? E/H\n :")
    if onay == 'e' or onay == 'E':
        continue
    else:
        print("İyi Günler")
        break



