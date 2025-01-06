import time
import datetime
import threading

#afficher_heure()

#alarme
def alarme(heure_alarme):
    while True:
        maintenant = datetime.datetime.now().strftime("%H:%M:%S")
        if maintenant == heure_alarme:
            print("\nAlarme ! Il est temps de se réveiller !")
            break
        #time.sleep(1)



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

        maintenant = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Heure actuelle : {maintenant}", end="\r")
        #time.sleep(1)

        if check_alarm(alarm_time):
            print("Alarme ! Il est temps de se réveiller !")
        time.sleep(1)

if __name__ == "__main__":
    main()

