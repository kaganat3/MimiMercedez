#Napiši program koji učitava prirodni broj n, a potom još n prirodnih brojeva. Program treba ispisati ukupan zbroj svih prvih i zadnjih znamenaka učitanih brojeva. Znamenka jednoznamenkastog broja gleda se samo jednom.
n=int(input("Upiši koliko brojeva želiš:"))
zbrj=0
for i in range(n):
    a=int(input("Upiši broj:"))
    b=a
    l=[]
    while(b>0):
        l.append(b%10)
        b//=10
    if(len(l)==1):
        zbrj+=a
    else:
        zbrj+=l[0]
        zbrj+=l[len(l)-1]
print(zbrj)
