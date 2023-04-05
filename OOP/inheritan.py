class Calisan():
    def __init__(self,isim,maas,departman):

        self.isim=isim
        self.maas=maas
        self.departman=departman

    def Yaz(self):

        print("İsim:"+self.isim)
        print("Maaş:"+str(self.maas))
        print("Departman:"+self.departman)

    def Zam(self,zam):

        self.maas += zam

    def departdegis(self,yeni_departman):

        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayi):

        super().__init__(isim,maas,departman)
        self.kisi_sayi=kisi_sayi #ek özellik

    def Yaz(self):

        print("İsim:" + self.isim)
        print("Maaş:" + str(self.maas))
        print("Departman:" + str(self.departman))
        print("Çalışan Sayısı:"+str(self.kisi_sayi))

    def CalisanArtir(self,arttir):
        self.kisi_sayi += arttir






calisan=Calisan("Cihan Gemi",50000,"Netwok Engineer")
calisan.Yaz()
reis =Yonetici("A G",12055555,"Patron",5000)
reis.Yaz()
reis.CalisanArtir(10)
reis.Yaz()





