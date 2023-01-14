def ort(vize, final):


    nott =float(((40*vize)/100)+((60*final)/100))
    if 88 <= nott and nott <= 100:
        print("Notunuz {} ,AA".format(nott))
        return nott
    elif 81 <= nott and nott <= 87:
        print("Notunuz {} ,BA".format(nott))
        return nott
    elif 74 <= nott and nott <= 80:
        print("Notunuz {} ,BB".format(nott))
        return nott
    elif 67 <= nott and nott <= 73:
        print("Notunuz {} ,CB".format(nott))
        return nott
    elif 60 <= nott and nott <= 66:
        print("Notunuz {} ,CC".format(nott))
        return nott
    elif 53 <= nott and nott <= 59:
        print("Notunuz {} ,DC".format(nott))
        return nott
    elif 46 <= nott and nott <= 52:
        print("Notunuz {} ,DD".format(nott))
        return nott
    elif 39 <= nott and nott <= 45:
        print("Notunuz {} ,FD".format(nott))
        return nott
    else:
        print("Notunuz {},FF".format(nott))
        return nott


vize1=float(input("Vizeniz:"))
final1=float(input("final:"))
sonuc= ort(vize1, final1)