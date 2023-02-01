sozluk = {"Huy":"insanın yaradılış ve ruhsal özelliklerinin, kendine özgülüklerinin tümü.",
          "Emrivaki":"oldubitti,olupbitti.",
          "İftira":"bir kimseye gerçek olmayan, olumsuz bir durumu, bir suçu, amaçlı olarak, bilerek yükleme, kara çalma.",
          "astigmat":"duru göremeyen(göz)",
          "baki":"sürekli,kalıcı",
          "cefa":"Semt ismi ;)"}

print("Türkçe Sözlük \n")

while(True):
    search = input("Aradığınız kelime:")
    sayac = 0

    for i, j in (sozluk.items()):

        if search != i:
            sayac = sayac + 1
            continue
        else:

            print(j + "\n" )

    if sayac == 6:
        print("Kelime Henüs sözlüğümüze eklenmedi")


    print("Başka arama yapmak ister misniz? E-H")
    sec=input()
    if sec == "E" or sec == "e" :
        continue

    else:
        print("See you later")
        break
