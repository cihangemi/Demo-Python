#Faktöriyel hesaplama
faktor=1
while(True):
    sayi = int(input("0 dan büyük sayi gir:"))
    if (sayi<=0):
        print("0'dan büyük sayi girin")
    else:
        for i in range(1,sayi+1):
            faktor *= i
         # ( faktor *=i )   == (faktor = faktor*i)
        print("Sonuc=",faktor)
        break
