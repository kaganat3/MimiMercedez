#Napiši program koji učitava prirodni broj n i zatim listu od n cijelih brojeva. Na temelju te liste kreiraj drugu listu čiji će prvi element bit jednak sumi svih elemenata prve liste, drugi element jednak sumi prvih n-1 elemenata liste itd. Napiši tako kreiranu listu.
n=int(input("Upiši kolko br:"))
l=[]
for i in range(n):
    l.append(int(input("Upiši broj:")))
rjes=[]
while(len(l)>0):
    a=0
    for i in l:
        a+=i
    rjes.append(a)
    b=len(l)
    l.pop(b-1)
    print(rjes)
print(rjes)
