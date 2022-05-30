#Napiši program koji učitava broj zapisan u binarnome brojevnom sustavu, a ispisuje ga u dekadskome brojevnom sustavu.
bina=int(input("Upiši binarni broj:"))
b=[]
while(bina>0):
    b.append(bina%10)
    bina//=10
a=0
b.reverse()
for i in range(len(b)):
    if(i==0):
        a=0*2+b[0]
    else:
        a=a*2+b[i]
print(a)
