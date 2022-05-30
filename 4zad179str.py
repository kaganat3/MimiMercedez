#Napiši program koji učitava prirodni broj n i zatim listu od n cijelih brojeva. Program treba ispisati učitanu listu i ispisati koliko je elemenata liste manje od prosječne vrijednosti elemenata u učitanoj listi.
n=int(input("Upiši brj:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši neki broj:")))
print(l)
koliko=0
pros=0
for i in l:
    koliko+=1
    pros+=i
pros=pros/koliko
kolikomanje=0
for i in l:
    if(i<pros):
        kolikomanje+=1
print(kolikomanje)
