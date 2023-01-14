  # While    Calculator
print("Calculatorle bakam")

print("Toplama için:+\n Çıkarma için:-\n Çarpma için:*\n Bölne için:/\n")

while(True):
    sayi1 =int(input("1.sayi:"))
    sayi2 = int(input("2.sayi:"))
    choose = input("Yapmak istediğiniz işlem:")
    if choose=='+':
        sonuc=sayi1+sayi2
        print("Sonuç:{}".format(sonuc))
    elif choose=='-':
        sonuc=sayi1-sayi2
        print("Sonuç:{}".format(sonuc))
    elif choose=='*':
        sonuc=sayi1*sayi2
        print("Sonuç:{}".format(sonuc))
    elif choose=='/':
        sonuc=sayi1/sayi2
        print("Sonuç:{}".format(sonuc))
    else:
        print("hata 404")
    cevap=input("Başka islem yapmak istermisiniz? E/H\n :")
    if cevap=='e' or cevap=='E':
        continue
    else:
        print("bizi tercih ettiğiniz için teşkür")
        break