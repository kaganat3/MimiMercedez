#Napiši program koji će učitavati stringove koji sadrže ime i prezime osoba i ispisivati prezime i inicijal imena.
#Unos završava kada se učita string KRAJ.
n=input("Upiši nečije ime i prezime:")
imenaip=(n)
while(n!="KRAJ"):
    n=input("Upiši ime i prezime:")
    if(n=="KRAJ"):
        break
    else:
        imenaip+=","
        imenaip+=n
imenaip=imenaip.split(",")
for i in range(len(imenaip)):
    a=str(imenaip[i])
    a=a.split(" ")
    b=a[0]
    print(a[1],b[0])
