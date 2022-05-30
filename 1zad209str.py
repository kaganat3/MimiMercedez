#Edi voli čitati lektiru, ali još više proučavati značajke riječi i rečenica. Upravo se bavi analizom broja samoglasnika i suglasnika.
#Pomogni Ediju i napiši program koji će za učitani string ispisati koliko u njemu ima samoglasnika i koliko suglasnika.
a=input("Upiši string riječi:")
a=a.split(" ")
rjes=0
samo=["a","e","i","o","u","A","E","I","O","U"]
b=[]
for i in a:
    b.append(list(i))
novalis=[]
for i in range(len(b)):
    for j in b[i]:
        novalis.append(j)
for i in novalis:
    if i in samo:
        rjes+=1
print("Ima",rjes,"samoglasnika")
print("Ima",len(novalis)-rjes,"suglasnika")
