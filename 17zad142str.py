#Napiši program koji učitava prirodni broj n. Program treba ispisati sumu znamenki u binarnome zapisu broja n.
n=int(input("Upiši broj:"))
rjes=[]
while(n>1):
    if(n%2==0):
        rjes.append(0)
        n//=2
    else:
        rjes.append(1)
        n//=2
rjes.append(1)
rjes.reverse()
suma=0
print("Binarni zapis je:",end="")
for i in rjes:
      print(i,end="")
print("")
for i in rjes:
    suma+=i
print("Suma znamenaka je",suma,".")
