import time

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
