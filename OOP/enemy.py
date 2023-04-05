
"_init_ nesneler yaratılınca ilk çağrılan ilk fonksiyon"

import random
class Dusman:
    def __init__(self,isim,kalan_can,saldiri_gücü,mermi_sayisi,atis=random.randrange(10,20)):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldiri_gücü=saldiri_gücü
        self.mermi_sayisi=mermi_sayisi
        self.atis=atis
    def print(self):
        print("İnfo\n")
        print("Ad:"+str(self.isim))
        print("Can:"+str(self.kalan_can))
        print("Power:"+str(self.saldiri_gücü))
        print("Ammo:"+str(self.mermi_sayisi))
        print("------------------")
    def Saldir(self):
        print(self.isim+"--->Ştrauvv")

        print(str(self.atis)+"Mermi attın")
        self.mermi_sayisi -= self.atis
        return (self.atis,self.saldiri_gücü)
    def Vurul(self,atis,saldiri_gücü):
        print(self.isim+": Ah galbimmm.:(")
        self.kalan_can -= (atis * saldiri_gücü)
    def AmmoSayisi(self):
        if(self.mermi_sayisi < 0):
            print(self.isim+": Mermi bitti mermi")

        elif(self.mermi_sayisi > 0):
            print(self.isim+":"+str(self.mermi_sayisi)+"Mermi kaldı")
    def Yasiormu(self):
        if(self.kalan_can < 0):
            print("Topragı bol olsun")
        elif(self.kalan_can > 0):
            print(str(self.kalan_can)+"Canım var hala xD")










