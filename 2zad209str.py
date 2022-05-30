#Naš se Edi posvetio traženju najdulje i najkraće riječi u rečenici, što može biti zamorno.
#Puno elegantnije bilo bi da Edi ima programsko rješenje koje će obaviti tu zadaću.
#Napiši program koji će u učitanoj rečenici pronaći riječ koja je najdulja, odnosno najkraća i ispisati je, i ispisati koliko slova sadržava i na kojemu se mjestu nalazi u rečenici.
rec=input("Upiši rečenicu:")
rec=rec.split(" ")
zapamtid=[0,0,0]
if(len(rec)==1):
    print("Ima jedna riječ")
else:
    for i in range(len(rec)):
        if(len(rec[i])>zapamtid[0]):
            zapamtid[0]=len(rec[i])
            zapamtid[1]=rec[i]
            zapamtid[2]=i+1
            print("Najdulja riječ je","'",zapamtid[1],"'",", nalazi se na",zapamtid[2],"mjestu u rečenici")
    zapamtik=[zapamtid[0],0,0]
    for i in range(len(rec)):
        if(len(rec[i])<zapamtik[0]):
            zapamtik[0]=len(rec[i])
            zapamtik[1]=rec[i]
            zapamtik[2]=i+1
    if(zapamtik[1]==0):
        print("Sve riječi su iste duljine")
        print("Najkraća riječ je","'",zapamtid[1],"'",", nalazi se na",zapamtid[2],"mjestu u rečenici")
    else:
        print("Najkraća riječ je","'",zapamtik[1],"'",", nalazi se na",zapamtik[2],"mjestu u rečenici")
