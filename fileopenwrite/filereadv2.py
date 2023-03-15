with open("hector.txt","r") as dosya:
    dosya.seek(10)
    str1=dosya.read(13)
    dosya.seek(31)
    str2=dosya.read(3)
    dosya.seek(41)
    str3=dosya.read(6)
    print(str1+"\n",str2+"\n",str3+"\n")