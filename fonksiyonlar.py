def Hello():
    print("HelloWorld!")




def fakto(sayi):
    fakt = 1
    for i in range(1,sayi+1):
        fakt *= i
    return fakt



Hello()

cevap = int(input("Hesaplanacak sayi="))

a=fakto(cevap)
print(a)