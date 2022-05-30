#Napiši program koji učitava prirodni broj n i zatim dvije liste od n cijelih brojeva.
#Na temelju tih listi formiraj treću listu tao da svaki element nove list bude veći od odgovarajućih elemenata u učitanim listama.
#Ako su odgovarajući elementi u učitanim listama jednaki, onda u novu listu unesi broj 12.
#Ispiši listu
a=int(input("Upiši koliko znamenaka želiš"))
m=[]
n=[]
for i in range(a):
    m.append(int(input("Upiši br za 1. listu:")))
    n.append(int(input("Upiši br za 2. listu:")))
rjes=[]
for i in range(a):
    if(m[i]==n[i]):
        rjes.insert(i,12)
    else:
        rjes.insert(i,(max(m[i],n[i])+1))
print(m,n)
print(rjes)
    
