import time #sert a utiliser time.sleep

def heure_voulu(): #Choix heure auto ou configurer
    check = 0
    while check == 0:
        val = str(input("Voulez vous une heure prés définie ? (Y ou N) : "))
        if val == "Y" or val == "y" or val == "N" or val == "n":
            check = 1
        else :
            print("Valeur incorrect")
    return val

def afficher_heure(): #Réglage de l'heure
    check = 0
    while check == 0:
        val1 = int(input("Rentrez une heure : "))
        val2 = int(input("Rentrez les minutes : "))
        if val1 < 0 or val1 > 24 or val2 < 0 or val2 > 60 :
            print("Valeur invalide")
        else :
            check = 1
    val3 = 00
    horaire = (val1, val2, val3)
    return horaire

veref = heure_voulu()

if veref == "y" or veref == "Y": #Horloge préconfiguré
    while True:
        time_live = time.strftime("%H:%M:%S")
        print(f"{time_live}", end="\r")
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

    while True: #Boucle affichage de l'heure
        print("{H}:{M}:{S}".format(H = heure, M = minute, S = seconde), end="\r") #affiche l'heure sur une seule ligne
        s += 1
        seconde = chr(ord(val_s)+s) # +1 a la valeur ascii
        seconde = "%02d" % s
        if s == 60:
            m += 1
            s = 0
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
        time.sleep(1)