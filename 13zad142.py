#Napiši program koji učitava prirodni broj n i zatim još n prirodnih brojeva. Program treba ispisati:
#1) Koliko učitanih brojeva ima prvu i zadnju znamenku parnu
#2) Koliko učitanih brojeva ima točno jednu prostu znamenku
#3) Koliko je brojeva bilo 'little'. Broj je 'little' ako su mu sve znamenke manje ili jednake od tri.
n=int(input("Upiši koliko brojčeka želiš:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj:")))
#a
lista=[]
rjes=0
for i in l:
    a=i
    while(a>0):
        lista.append(a%10)
        a//=10
    if((lista[0]%2)==0 and (lista[len(lista)-1])%2==0):
       rjes+=1
print("Ima",rjes,"brojeva s prvom i zadnjom znamenkom parnom")
    
