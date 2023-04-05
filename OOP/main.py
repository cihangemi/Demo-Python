"NESNE TABANLI PROGLAMA -OOP-"
class Enemy:
    r_life=3
    "Self=kendi nesnemizi ifade eden anahtar kelime self.power gibi misal"
    def attack(self):
        print("Smash")
        self.r_life -=1
    def aLive(self):
        if(self.r_life == 0):
            print("Lose")
        else:
            print("Not yet ;)"+str(self.r_life))

enemy1=Enemy()
enemy2=Enemy()
enemy1.attack()
enemy1.attack()
enemy1.aLive()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy2.aLive()


