#Çoklu Kalıtım Örnek
#Pek Önerilmiyor
class Ogrenci():
    def derscalis(self):
        print("Ögrenci ders çalişior")

class Calisan():
    def calis(self):
        print("Personel çalışıyor")


class Yazılımcı(Ogrenci,Calisan):
    def derscalis(self):
        print("Yazlimci ders çalışıo")




yazilimci=Yazılımcı()
yazilimci.calis()
yazilimci.derscalis()
