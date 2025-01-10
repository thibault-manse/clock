import time
import datetime #datetime est un outil puissant pour manipuler les dates et les heures

#afficher_heure()
def afficher_heure():
    while True :
        heure_actuelle = time.strftime("%H:%M:%S")
        print(f"heure_actuelle : {heure_actuelle}", end="\r")
        time.sleep()


def set_alarm():
    alarm_time = input("Entrez l'heure de l'alarme (HH:MM:SS): ")
    return alarm_time

def check_alarm(alarm_time):
    current_time = time.strftime("%H:%M:%S")
    return current_time == alarm_time

def main():
    alarm_time = set_alarm()
    print(f"Alarme réglée pour {alarm_time}.")

    while True:

        maintenant = datetime.datetime.now().strftime("%H:%M:%S") #est utilisé pour obtenir dates et heures actuelle
        print(f"Heure actuelle : {maintenant}", end="\r") # le end= signifie que tout sera imprimé sur la même ligne.
        #time.sleep(1)

        if check_alarm(alarm_time):
            print("Alarme ! Il est temps d'aller à la plateforme ! ")
        time.sleep(1) # la fonction sleep est utilisée pour mettre en pause l'exécution d'un programme durant quelques secondes
        

if __name__ == "__main__":
    main()

