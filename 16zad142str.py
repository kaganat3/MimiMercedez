#Napiši program koji učitava prirodni broj n i iz njega izbacuje sve znamenke na neparnim mjesitma. Iz tako dobivenog broja ponovo treba izbaciti sve znamenke na isti način.
#Sve to treba ponavljati dok broj ne postane jednoznamenkast. Program treba ispisati tako dobiveni jednoznamenkasti broj.
n=int(input("Upiši broj"))
l=[]
while(n>0):
    l.append(n%10)
    n//=10
l.reverse()
a=0
while(len(l)>1):
    a+=1
    parniindexi=[]
    a=len(l)
    for i in range(a):
        if((i+1)%2!=0):
            parniindexi.append(i)
    for i in range(len(parniindexi)):
        l.pop(parniindexi[i])
        for k in range(len(parniindexi)):
                parniindexi[k]=parniindexi[k]-1
print(l)
