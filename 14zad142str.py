#Napiši program koji učitava dva različita prirodna broja m i n. Program treba ispisati sve brojeve između m i n takve da im je zbroj znamenki prost broj. Ako ne postoji niti jedan takav broj, program treba ispisati odgovarajuću poruku.
n=int(input("Upiši prvi broj:"))
m=int(input("Upiši drugi broj:"))
rjes=0
brojac=0
for i in range(min(n,m)+1,max(n,m)):
    l=[]
    a=i
    b=0
    brj=0
    while(a>0):
        l.append(a%10)
        a//=10
    for j in l:
        b+=j
    for k in range(b):
        if(b%(k+1)==0):
            brj+=1
    if(brj==2):
        print(i)
        brojac+=1
if(brojac==0):
    print("Ne postoji takav broj")
