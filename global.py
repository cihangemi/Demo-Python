a=10
b=2

def globalexamp() :
    a=3
    #Global komutu fonksiyon dışındaki değeri değiştirir
    global b
    b=4
    print("Fonksiyon içi: ",a,b)

globalexamp()
print("Global:",a,b)