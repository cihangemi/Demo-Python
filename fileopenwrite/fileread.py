dosya = open("hector.txt","r")
#print(dosya.read())
#print(dosya.readlines())
liste =dosya.readlines()
print(liste[1])
for i in  range(len(liste)):
    print(liste[i])

dosya.close()