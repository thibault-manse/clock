import time #sert a utiliser time.sleep
import os #sert a effacer le terminal grace a os.system('cls')


def AMPM_demande():
    global format_12h
    format_12h=None
    while format_12h==None:
        AMPM_check=input("Voulez vous un format AM/PM? (Y/N)").upper()
        if AMPM_check !="N" and AMPM_check!="Y":
            print("Réponse invalide, veuillez utiliser Y ou N.")

        elif AMPM_check=="Y":
            format_12h=True

        elif AMPM_check=="N":
            format_12h=False




def heure_voulu(): #Choix heure auto ou configurer
    check = 0
    while check == 0:
        val = str(input("Voulez vous une heure prédéfinie ? (Y ou N) : ")).upper()
        if val == "Y" or val == "N":
            check = 1
        else :
            print("Valeur incorrect")
    return val

def afficher_heure(): #Réglage de l'heure
    check = 0
    while check == 0:
        global val1
        val1 = int(input("Rentrez une heure : "))
        val2 = int(input("Rentrez les minutes : "))
        if val1 < 0 or val1 > 24 or val2 < 0 or val2 > 60 :
            print("Valeur invalide")
        else :
            check = 1
        
        if format_12h==True:
            global AMPM
            AMPM=None
            while AMPM==None:
                AMPM=input("AM ou PM?").upper()
                if AMPM!="AM" and AMPM!="PM":
                    print("Écrire 'AM' ou 'PM' s'il vous plaît")

            while val1>12 or val1<0:
                print("entrez une valeur entre 12 et 0 s'il vous plaît")
                val1 = int(input("Rentrez une heure : "))
    val3 = 00
    horaire = (val1, val2, val3)


    return horaire

AMPM_demande()
veref = heure_voulu()


if veref == "Y": #Horloge préconfiguré
    while True:
        temps = time.strftime("%H:%M:%S")

        if format_12h==True:
            if int(time.strftime("%H"))>=12:
                    AMPM="PM"
                    if int(time.strftime("%H"))==12:
                        print("12:"+time.strftime(":%M:%S"), AMPM, end="\r")
                    elif int(time.strftime("%H"))-12==10 or int(time.strftime("%H"))-12==11 or int(time.strftime("%H"))-12==12:
                        print(int(time.strftime("%H"))-12,":", int(time.strftime("%M")),":",int(time.strftime("%S")) ,AMPM,"                                 ", end="\r")
                    else:
                        print(int(time.strftime("%H"))-12,":", int(time.strftime("%M")),":",int(time.strftime("%S")) ,AMPM,"                                 ", end="\r")

                    
            elif int(time.strftime("%H"))==0:
                AMPM="AM"
                print("12:", time.strftime(":%M:%S"), AMPM, end="\r")

            elif int(time.strftime("%H"))-12<=0:
                AMPM="AM"
                print(f"{temps}", AMPM, end="\r")

        else:
            print(f"{temps}", end="\r")
        time.sleep(1)


            


else : #Horloge configurer
    h, m, s = afficher_heure()

    #Afficher 01:00:00 et non 1:0:0 (transformer en str)
    val_h = str(0)
    val_m = str(0)
    val_s = str(0)

    heure = "%02d" % h
    minute = "%02d" % m
    seconde = "%02d" % s
    #-----------------------------

    os.system('cls')

    while True: #Boucle affichage de l'heure

        s += 1
        seconde = chr(ord(val_s)+s) # +1 a la valeur ascii
        seconde = "%02d" % s
        if s == 60:
            m += 1
            s =0
            minute = chr(ord(val_m)+m)
            minute = "%02d" % m
            seconde = "%02d" % 0
            if m == 60:
                h += 1
                m = 0
                heure = chr(ord(val_h)+h)
                heure = "%02d" % h
                minute = "%02d" % 0
                if h == 24:
                    h = 0
                    heure = "%02d" % 0
        if m==0 and s==0:
            os.system("cls")
        if format_12h==True:
            
            if h>=12:
                AMPM="PM"
                print("{H}:{M}:{S}".format(H = heure, M = minute, S = seconde), AMPM ,"                                  ", end="\r")
                if h>=13:
                    print(f"{int(heure)-12}:""{M}:{S}".format( M = minute, S = seconde), AMPM,"                          ", end="\r")
            elif h==0:
                AMPM="AM"
                print("12:{M}:{S}".format( M = minute, S = seconde) , AMPM,"                                           ", end="\r")

            elif h-12<=0:
                AMPM="AM"
                print("{H}:{M}:{S}".format(H = heure, M = minute, S = seconde), AMPM,"                                        ", end="\r")
        else:
            print("{H}:{M}:{S}".format(H = heure, M = minute, S = seconde), "                                    ", end="\r") #affiche l'heure sur une seule ligne
            

        
        time.sleep(1)