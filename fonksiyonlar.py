def Hello():
    print("HelloWorld!")




def fakto(sayi):
    fakt = 1
    for i in range(1,sayi+1):
        fakt *= i
    print("Sonuç=",fakt)



Hello()

cevap = int(input("Hesaplanacak sayi="))
fakto(cevap)
