import time #sert a utiliser time.sleep
from datetime import datetime
import keyboard
from threading import Event

paused = False 
pause_event = Event()

def heure_voulu(): #Choix heure auto ou configurer
    check = 0
    while check == 0:
        val = str(input("Voulez vous une heure prédéfinie ? (Y ou N) : ").lower())
        if val in ("y", "n"):
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
        time.sleep(1)

def toggle_pause(e):
    global paused
    paused = not paused
    if paused:
        pause_event.clear()
    else:
        pause_event.set()
    print("\nHorloge en pause" if paused else "\nHorloge en marche")


# Demander à l'utilisateur s'il souhaite régler une alarme
def main():
    
    global paused
    pause_event.set()
    
    keyboard.on_press_key("space", toggle_pause)
    print("\nAppuyez sur 'espace' pour mettre en pause/reprendre")
    
    choice = input("Voulez-vous régler une alarme ? (oui/non): ").lower()
    if choice == "oui":
        set_alarm()
    else:
        print("vous n'avez pas prédéfini d'alarme. Au revoir!")


    try:
        if veref == "y": #Horloge préconfiguré
            pause_time = None
            initial_time = None
            
            while True:
                if not paused:
                    if pause_time is not None:
                        # Calculer le décalage depuis la pause
                        offset = time.time() - pause_time
                        initial_time = time.time() - offset
                        pause_time = None
                    
                    if initial_time is None:
                        initial_time = time.time()
                        
                    current_time = time.localtime(initial_time)
                    temps = time.strftime("%H:%M:%S", current_time)
                    print(f"{temps}", end="\r")
                    initial_time += 1
                    time.sleep(1)
                else:
                    if pause_time is None:
                        pause_time = time.time()
                    time.sleep(0.1)

        else: #Horloge configurer
            h, m, s = afficher_heure()
            paused_time = None

            while True: #Boucle affichage de l'heure
                if not paused:
                    if paused_time is not None:
                        # Reprendre depuis l'heure de pause
                        h, m, s = paused_time
                        paused_time = None
                        
                    print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")
                    s += 1
                    if s == 60:
                        m += 1
                        s = 0
                        if m == 60:
                            h += 1
                            m = 0
                            if h == 24:
                                h = 0
                    time.sleep(1)
                else:
                    if paused_time is None:
                        paused_time = (h, m, s)
                    time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAu revoir!")
    finally:
        keyboard.unhook_all()
                
            
# Exécuter le programme
if __name__ == "__main__":
    main()