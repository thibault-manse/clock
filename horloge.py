import time #import de "time" pour les fonctionnalitées de temps
import os #import de "os" pour le commande "cls"


def horloge():
    os.system("cls") #efface les info de l'ordinatuer (C/fichier/ficher etc.)


    alarme_existe=False #boolean pour indiquer si une alarme existe ou non

    reglage_manuel=False #boolean pour indiquer si le mode de reglage est manuel ou automatique

    mode_AMPM=False #boolean pour indiquer si l'horloge est en mode AMPM ou 24h

    #decider si le mode d'affichage est en 24h ou AMPM
    mode_affiche=input("voulez vous avoir un mode d'affichage AM/PM?")

    os.system("cls")

    if mode_affiche=="oui" or mode_affiche=="yes" or mode_affiche=="y":
        mode_AMPM=True
    else:
        mode_AMPM=False

    #decider si une alarme est demandé
    alarme_choix=input("voulez vous ajouter un alarme?")
    
    if alarme_choix=="oui" or alarme_choix=="yes" or alarme_choix=="y":
        alarme_heure=int(input("quel heure?"))
        if mode_AMPM==True:
            alarme_AMPM=input("AM ou PM?").upper()
            if alarme_AMPM!="AM" and alarme_AMPM!="PM":
                print("seulement AM ou PM s'il vous plaît")
                alarme_AMPM=input("AM ou PM?")
        alarme_minute=int(input("quel minute?"))
        alarme_existe=True
        
        os.system("cls")

    else:
        alarme_heure=None
        alarme_minute=None
        alarme_existe=False
        os.system("cls")

    #demander si le mode de reglage est maneul ou automatique
    mode_de_regle=input("voulez vous regler l'horloge par vous même?")

    if mode_de_regle=="oui" or mode_de_regle=="yes" or mode_de_regle=="y":
        reglage_manuel=True
        heurem=int(input("il est quel heure maintenant?"))
        if mode_AMPM==True:
            heurem_AMPM=input("AM ou PM?").upper()
            if heurem_AMPM!="AM" and heurem_AMPM!="PM":
                print("seulement AM ou PM s'il vous plaît")
                alarme_AMPM=input("AM ou PM?").upper()
        minutem=int(input("il est quel minute maintenant?"))
        secondem=int(input("il est quel seconde maintenant?"))
        os.system("cls")
    
    else:
        reglage_manuel=False
        os.system("cls")

   
    #reglage automatique en format 24h
    while reglage_manuel==False and mode_AMPM==False:

        from datetime import datetime #importer le date et temps de "datetime"
        actuelle=datetime.now() #sortir le date et temps et le mettre dans le variable "actuelle"

        #afficher l'heure avec le date, %s indique des cases pour importer les data: .day .month .year
        print(" %s/%s/%s  %s:%s:%s" % (actuelle.day, actuelle.month, actuelle.year, actuelle.hour, actuelle.minute, actuelle.second))
        time.sleep(1)
        os.system("cls")
        
        #sonner l'alarme
        if alarme_existe==True and actuelle.hour==alarme_heure and actuelle.minute==alarme_minute:
            print(" L'ALARME SONNE!!!!!!!!!!!!!!!!!!")

    #reglage manuel en format 24h
    while reglage_manuel==True and mode_AMPM==False:
        print(f"{heurem}:{minutem}:{secondem}")
        secondem+=1
        if secondem==60:
             minutem+=1
             secondem=0
             if minutem==60:
                  heurem+=1
                  minutem=0
                  if heurem==24:
                       heurem=0
        time.sleep(1)
        os.system("cls")

        if alarme_existe==True and heurem==alarme_heure and minutem==alarme_minute:
            print(" L'ALARME SONNE!!!!!!!!!!!!!!!!!!")

    #reglage automatique en format AMPM
    while mode_AMPM==True and reglage_manuel==False:

        from datetime import datetime
        actuelle=datetime.now()
        if actuelle.hour-12<0:
            AMPM="AM"
            print(" %s/%s/%s  %s:%s:%s" % (actuelle.day, actuelle.month, actuelle.year, actuelle.hour, actuelle.minute, actuelle.second),AMPM)
        else:
            AMPM="PM"
            print(" %s/%s/%s  %s:%s:%s" % (actuelle.day, actuelle.month, actuelle.year, actuelle.hour-12, actuelle.minute, actuelle.second),AMPM)
        time.sleep(1)
        os.system("cls")

        if alarme_existe==True and actuelle.hour==alarme_heure and actuelle.minute==alarme_minute and AMPM==alarme_AMPM:
            print(" L'ALARME SONNE!!!!!!!!!!!!!!!!!!")

    #reglage manuel en format AMPM
    while reglage_manuel==True and mode_AMPM==True:
        from datetime import datetime
        actuelle=datetime.now()

        print(f"%s/%s/%s {heurem}:{minutem}:{secondem}" % (actuelle.day, actuelle.month, actuelle.year), heurem_AMPM )
        secondem+=1
        if secondem==60:
             minutem+=1
             secondem=0
             if minutem==60:
                  heurem+=1
                  minutem=0
                  if heurem==12:
                        if heurem_AMPM=="AM":
                           heurem_AMPM="PM"
                        elif heurem_AMPM=="PM":
                           heurem_AMPM="AM"
                  if heurem==13:
                    heurem=1

        time.sleep(1)
        os.system("cls")

        if alarme_existe==True and heurem==alarme_heure and minutem==alarme_minute:
            print(" L'ALARME SONNE!!!!!!!!!!!!!!!!!!")

horloge()