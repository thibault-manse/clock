import time #
import datetime
import threading

def heure_voulu(): #Choose auto time or configure
    check = 0
    while check == 0:
        val = str(input("Do you want a predefined time? (Y ou N) : "))
        if val == "Y" or val == "y" or val == "N" or val == "n":
            check = 1
        else :
            print("Invalid value")
    return val

def afficher_heure(): #Time setting
    check = 0
    while check == 0:
        val1 = int(input("Come home for an hours : "))
        val2 = int(input("Come home for an minutes: "))
        if val1 < 0 or val1 > 24 or val2 < 0 or val2 > 60 :
            print("Invalid Value")
        else :
            check = 1
    val3 = 00
    horaire = (val1, val2, val3)
    return horaire

veref = heure_voulu()

# Function to display the clock in real time
def display_clock():
    while True:
        # Get the current time with datetime
        current_time = datetime.datetime.now()
        
        # Display of the current time (hour, minute, second)
        print(f"current time : {current_time.strftime('%H:%M:%S')}", end="\r")
        
        # Wait 1 second before updating the time
        time.sleep(1)

# Function to set alarm
def set_alarm():
    print("welcome to the alarm: ")
    
    # Request alarm time in HH:MM format
    alarm_time = input("Enter the alarm time (HH:MM): ")
    
    # Format check. split = the separator used to split the string (maximum number of divisions. -1 default means no limit)
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        
        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
            print("The hour or minutes are invalid. Please enter a valid time.")
            return
    except ValueError:
        print("The time format is incorrect. Be sure to enter the time in the HH:MM format.")
        return
    
    # Display the time chosen for the alarm
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

    # Start the clock in real time in a separate thread
    clock_thread = threading.Thread(target=display_clock, daemon=True)
    clock_thread.start()

    # Loop to check the current time and alarm
    while True:
        # Get the current time with datetime
        current_time = datetime.datetime.now()
        
        # Check if the current time matches the alarm time
        if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
            print(f"\nIl est {current_time.strftime('%H:%M:%S')}. It's time to go to the platform!")
            break  # Break out of the loop when the alarm goes off
        
        # Wait 0.1 seconds before checking the time again (to avoid consuming too many resources)
        time.sleep(0.1)

# Ask the user if they want to set an alarm
def main():
    choice = input("Do you want to set an alarm? (yes/no): ").lower()
    if choice == "yes":
        set_alarm()
    else:
        print("You have not preset an alarm. Goodbye and godbless!")

# Execute the program
if __name__ == "__main__":
    main()

