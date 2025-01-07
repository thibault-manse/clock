import datetime
import time

def afficher_heure_actuelle():
    while True:
        maintenant = datetime.datetime.now()
        print(maintenant.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

def définir_alarme(heure_alarme):
    while True:
        maintenant = datetime.datetime.now()
        heure_actuelle = maintenant.strftime("%H:%M:%S")
        if heure_actuelle == heure_alarme:
            print("\nAlarme ! Il est l'heure :", heure_alarme)
            break
        time.sleep(1)

def main():
    print("Bienvenue dans l'horloge avec alarme !")
    heure_alarme = input("Veuillez entrer l'heure de l'alarme (HH:MM:SS) : ")
    print("L'alarme est réglée pour :", heure_alarme)
    
    # Démarrer l'affichage de l'heure actuelle dans un thread séparé
    import threading
    thread_heure = threading.Thread(target=afficher_heure_actuelle)
    thread_heure.daemon = True
    thread_heure.start()
    
    # Démarrer la vérification de l'alarme
    définir_alarme(heure_alarme)

if __name__ == "__main__":
    main()
