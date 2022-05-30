#Napiši program koji će iz učitanog stringa ukloniti sve pojave zadanog podstrniga.
a=input("Upiši neki string:")
podstr=input("Upiši neki podstring:")
for i in a:
    if i in podstr:
        a=a.replace(i,"")
print(a)
