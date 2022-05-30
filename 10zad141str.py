#Napiši program koji će unositi prirodan broj n. Program treba provjeriti je li uneseni broj palindrom.
n=int(input("Upiši prirodan broj:"))
a=n
broj=[]
while(a>0):
    broj.append(a%10)
    a//=10
obrnuto=broj[::-1]
for i in range(len(broj)):
    if(broj[i]==obrnuto[i]):
        a+=1
if(a==len(broj)):
    print("Palindrom je")
else:
    print("Nije palindrom")
