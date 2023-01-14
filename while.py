#Kullanıcı Adı Parola
defuser="hector"
defpassw="11111"
while(True):
    user = input("Kullanici Adiniz:")
    passw = input("Sifreniz:")
    if ((defuser == user)and(defpassw == passw)):
        print("Hosgeldiniz\n {}".format(defuser))
        break
    elif (defuser != user):
        print("Kullanici adi hatali !")
    elif(defpassw != passw):
        print("Yanlis Sifre")
        print("Sifrenizi sifirlamak ister misiniz ? Y/N")
        answ = input()
        if(answ == 'Y' or 'y'):
            nevpassw = input("Yeni sifrenizi girin:")
            defpassw = nevpassw
    else:
        print("Try Again")



