#Napiši program koji učitava prirodni broj n, a potom n prirodnih brojeva strogo većih od 10.
#Program treba ispisati koliko učitanih brojeva ima prostu drugu znamenku (onu s drugom najvećom težinom u broju)
n=int(input("Upiši broj:"))
a=10
l=[]
for i in range(n):
    a+=1
    l.append(a)
brojac=0
lista=[]
for i in l:
    a=i
    while(a>0):
        lista.append(a%10)
        a//=10
    b=lista.pop(1)
    br=0
    for j in range(b):
        if(b%(j+1)==0):
            br+=1
    if(br==2):
        brojac+=1
print(brojac)
    
    
