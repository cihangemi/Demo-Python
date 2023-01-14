def kok(a,b,c):
    if a!=0 and b!=0 and c!=0:
        delta=((b*b)-(4*a*c))
        if delta > 0 :
            print("İki farklı reel kök vardır")
            x1=((-b)+(delta**0.5))/(2*a)
            x2=((-b)-(delta*0.5))/(2*a)
            return x1,x2
        elif delta == 0:
            print("Çakışık iki kök var")
            x1=x2=(-b+delta*0.5)/2*a
            return x1,x2
        else:
            print("Gerçel kök yoktur")
            return
    elif b==0 and ((a<0 and c<0 )or (a>0 and c>0))   :
        print("reel kök yoktur")
    elif b==0:
        x1= -(-c/a)*0.5
        x2=(-c/a)*0.5
        return x1,x2
    elif b==0 and c==0:
        x1=0
        x2=0
        return x1,x2
    elif c==0:
        x1=0
        x2=-b/a
        return x1,x2

    else:
        print("error")

print("kökleri giriniz")
x=int(input("a:"))
y=int(input("b:"))
z=int(input("c:"))
sonuc =kok(x, y, z)
print("Kokleriniz:",sonuc)