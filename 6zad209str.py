#Napiši program koji će datum u formatu dan.mjesec godina pretvoriti u format dd.mm.gggg.
n=input("Upiši datum:")
n=n.replace("."," ")
n=n.split(" ")
mjesec=["siječanj","veljača","ožujak","travanj","svibanj","lipanj","srpanj","kolovoz","rujan","listopad","studeni","prosinac"]
for i in range(len(n)):
    if(i==0):
        print(n[0],".",end="")
    if(i==1):
        print(mjesec.index(n[1])+1,".",end="")
    if(i==2):
        print(n[2],".")
