import time #time library to use time.sleep()
import os #allows the program to clear the terminal using os.system('cls')


def AMPM_request():
    global ampm_format
    ampm_format=None
    while ampm_format==None:
        AMPM_check=input("Would you like to use the AM/PM format? (Y/N): ").upper()
        if AMPM_check !="N" and AMPM_check!="Y":
            print("invalid response. please enter Y or N")
            AMPM_check=input("Would you like to use the AM/PM format? (Y/N)").upper()

        elif AMPM_check=="Y":
            ampm_format=True

        elif AMPM_check=="N":
            ampm_format=False




def predefined_request(): #predefined time prompt
    check = 0
    while check == 0:
        val = str(input("Would you like a predefined clock? (Y or N) : ")).upper()
        if val == "Y" or val == "N":
            check = 1
        else :
            print("Incorrect value")
    return val

def manual_config(): #manual clock set up
    check = 0
    while check == 0:
        global val1
        val1 = int(input("Enter the hour : "))
        val2 = int(input("Enter the minute : "))
        if val1 < 0 or val1 > 24 or val2 < 0 or val2 > 60 :
            print("Invalid value")
        else :
            check = 1
        
        if ampm_format==True:
            global AMPM
            AMPM=None
            while AMPM==None:
                AMPM=input("AM or PM?").upper()
                if AMPM!="AM" and AMPM!="PM":
                    print("Please enter AM or AM")
                    AMPM=input("AM or PM?").upper()

            while val1>12 or val1<0:
                print("Please enter a value between 0 and 12")
                val1 = int(input("Enter the hour : "))
    val3 = 00
    mclock = (val1, val2, val3)


    return mclock

AMPM_request()
veref = predefined_request()


if veref == "Y": #Preconfigured clock
    while True:
        aclock = time.strftime("%H:%M:%S")

        if ampm_format==True:
            if int(time.strftime("%H"))>=12:
                    AMPM="PM"
                    if int(time.strftime("%H"))==12:
                        print("12:"+time.strftime(":%M:%S"), AMPM,"                         ", end="\r")
                    elif int(time.strftime("%H"))-12==10 or int(time.strftime("%H"))-12==11 or int(time.strftime("%H"))-12==12:
                        print(int(time.strftime("%H"))-12,":", int(time.strftime("%M")),":",int(time.strftime("%S")) ,AMPM,"                                 ", end="\r")
                    else:
                        print(int(time.strftime("%H"))-12,":", int(time.strftime("%M")),":",int(time.strftime("%S")) ,AMPM,"                                 ", end="\r")

                    
            elif int(time.strftime("%H"))==0:
                AMPM="AM"
                print("12:", time.strftime(":%M:%S"), AMPM, end="\r")

            elif int(time.strftime("%H"))-12<=0:
                AMPM="AM"
                print(f"{aclock}", AMPM, end="\r")

        else:
            print(f"{aclock}", end="\r")
        time.sleep(1)


            


else : #manual clock
    h, m, s = manual_config()

    #to show 01:00:00 and not 1:0:0 (transform into str)
    val_h = str(0)
    val_m = str(0)
    val_s = str(0)

    hour = "%02d" % h
    minute = "%02d" % m
    second = "%02d" % s
    #-----------------------------

    os.system('cls')

    while True: #clock loop

        s += 1
        second = chr(ord(val_s)+s) # +1 to the ascii value
        second = "%02d" % s
        if s == 60:
            m += 1
            s =0
            minute = chr(ord(val_m)+m)
            minute = "%02d" % m
            second = "%02d" % 0
            if m == 60:
                h += 1
                m = 0
                hour = chr(ord(val_h)+h)
                hour = "%02d" % h
                minute = "%02d" % 0
                if h == 24:
                    h = 0
                    hour = "%02d" % 0
        if m==0 and s==0:
            os.system("cls")
        if ampm_format==True:
            
            if h>=12:
                AMPM="PM"
                print("{H}:{M}:{S}".format(H = hour, M = minute, S = second), AMPM ,"                                  ", end="\r")
                if h>=13:
                    print(f"{int(hour)-12}:""{M}:{S}".format( M = minute, S = second), AMPM,"                          ", end="\r")
            elif h==0:
                AMPM="AM"
                print("12:{M}:{S}".format( M = minute, S = second) , AMPM,"                                           ", end="\r")

            elif h-12<=0:
                AMPM="AM"
                print("{H}:{M}:{S}".format(H = hour, M = minute, S = second), AMPM,"                                        ", end="\r")
        else:
            print("{H}:{M}:{S}".format(H = hour, M = minute, S = second), "                                    ", end="\r") #to show the clock on one line
            

        
        time.sleep(1)