import time

def afficher_heure():
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

h, m, s = afficher_heure()
val_h = str(0)
val_m = str(0)
val_s = str(0)

heure = "%02d" % h
minute = "%02d" % m
seconde = "%02d" % s

i = 0

while i < 1:
    print("{H}:{M}:{S}".format(H = heure, M = minute, S = seconde))
    s += 1
    seconde = chr(ord(val_s)+s)
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