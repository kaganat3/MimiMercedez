#Napiši program koji učitava prirodni broj n i zatim listu od n cijelih brojeva.
#Program treba ispisati:
#a)tri najmanja broja u učitanoj listi
#b)treću po veličini vrijednost koja se pojavljuje u učitanoj listi
n=int(input("Koliko cijelih br želiš?"))
l=[]
for i in range(n):
    l.append(int(input("Upiši cijeli br:")))
a=l
a.sort()
print("Tri najmanja broja su:",a[0],a[1],a[2])
a.reverse()
print("Treća po redu vrijednost je:",a[2])
