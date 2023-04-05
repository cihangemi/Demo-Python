"_init_ nesneler yaratılınca ilk çağrılan ilk fonksiyon"
class Dusman:
    def __init__(self,isim='Ganxboy',kalan_can=100,saldiri_gücü=15,mermi_sayisi=21):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldiri_gücü=saldiri_gücü
        self.mermi_sayisi=mermi_sayisi
    def print(self):
        print("İnfo")
        print(self.isim)
        print(self.kalan_can)
        print(self.saldiri_gücü)
        print(self.mermi_sayisi)

dusman=Dusman()
print("Default Düşman")
dusman.print()
dusman1=Dusman("Cartcix",31,100,1)
print("Manuel Düşman xD")
dusman1.print()


