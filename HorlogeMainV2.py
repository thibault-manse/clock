import time #sert a utiliser time.sleep

def heure_voulu(): #Choix heure auto ou configurer
    check = 0
    while check == 0:
        val = str(input("Voulez vous une heure prés définie ? (Y ou N) : ").lower())
        if val == "y" or val == "n":
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

# Fonction pour définir l'alarme
def set_alarm():
    print("Bienvenue dans l'alarme!")
    
    # Demander l'heure de l'alarme sous le format HH:MM
    alarm_time = input("Entrez l'heure de l'alarme (HH:MM): ")
    
    # Vérification du format
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        
        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
            print("L'heure ou les minutes sont invalides. Veuillez entrer une heure valide.")
            return
    except ValueError:
        print("Le format de l'heure est incorrect. Assurez-vous de saisir l'heure sous le format HH:MM.")
        return
    
    # Afficher l'heure choisie pour l'alarme
    print(f"Alarme définie pour {alarm_hour:02d}:{alarm_minute:02d}")

    # Boucle infinie pour vérifier l'heure actuelle
    while True:
        # Obtenez l'heure et les minutes actuelles
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        
        # Vérifiez si l'heure actuelle correspond à l'heure de l'alarme
        if current_hour == alarm_hour and current_minute == alarm_minute:
            print(f"Il est {current_hour:02d}:{current_minute:02d}. C'est l'heure d'aller à la plateforme !!")
            break  # Sort de la boucle une fois l'alarme déclenchée
        
        # Attendre 30 secondes avant de vérifier à nouveau l'heure
        time.sleep(30)

# Demander à l'utilisateur s'il souhaite régler une alarme
def main():
    choice = input("Voulez-vous régler une alarme ? (oui/non): ").lower()
    if choice == "oui":
        set_alarm()
    else:
        print("vous n'avez pas prédéfini d'alarme. Au revoir!")

# Exécuter le programme
if __name__ == "__main__":
    main()


if veref == "y" or veref == "Y": #Horloge préconfiguré
    while True:
        temps = time.strftime("%H:%M:%S")
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