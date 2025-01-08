import time #sert a utiliser time.sleep
import datetime
import threading

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

# Fonction pour afficher l'horloge en temps réel
def display_clock():
    while True:
        # Obtenez l'heure actuelle avec datetime
        current_time = datetime.datetime.now()
        
        # Affichage de l'heure actuelle (heure, minute, seconde)
        print(f"Heure actuelle : {current_time.strftime('%H:%M:%S')}", end="\r")
        
        # Attendre 1 seconde avant de mettre à jour l'heure
        time.sleep(1)

# Fonction pour définir l'alarme
def set_alarm():
    print("Bienvenue dans l'alarme!")
    
    # Demander l'heure de l'alarme sous le format HH:MM
    alarm_time = input("Entrez l'heure de l'alarme (HH:MM): ")
    
    # Vérification du format. split = le séparateur utilisé pour diviser la chaine ( nombre maximum de division. -1 la valeur par default signifie aucune limite)
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

    # Démarrer l'horloge en temps réel dans un thread séparé
    clock_thread = threading.Thread(target=display_clock, daemon=True)
    clock_thread.start()

    # Boucle pour vérifier l'heure actuelle et l'alarme
    while True:
        # Obtenez l'heure actuelle avec datetime
        current_time = datetime.datetime.now()
        
        # Vérifiez si l'heure actuelle correspond à l'heure de l'alarme
        if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
            print(f"\nIl est {current_time.strftime('%H:%M:%S')}. C'est l'heure d'aller à la plateforme !")
            break  # Sortir de la boucle lorsque l'alarme se déclenche
        
        # Attendre 0.1 secondes avant de vérifier à nouveau l'heure (pour éviter de consommer trop de ressources)
        time.sleep(0.1)

# Demander à l'utilisateur s'il souhaite régler une alarme
def main():
    choice = input("Voulez-vous régler une alarme ? (oui/non): ").lower()
    if choice == "oui":
        set_alarm()
    else:
        print("Vous n'avez pas prédéfini d'alarme. Au revoir!")

# Exécuter le programme
if __name__ == "__main__":
    main()

