#Napiši program koji unosi prirodni broj i ispisuje srednju znamenku tog broja ako broj ima neparan broj znamenaka, ili pak srednej dvije znamenke ako ima paran broj znamenka.
n=int(input("Upipi broj:"))
a=n
l=[]
while(a>0):
    l.append(a%10)
    a//=10
rjes=[]
if(len(l)%2==0):
    b=len(l)//2
    for i in range(2):
        rjes.append(l.pop(b-1))
    rjes.reverse()
else:
    b=len(l)//2
    rjes.append(l.pop(b))
print(rjes)
