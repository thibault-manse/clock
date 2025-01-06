import time

h = 23
m = 59
s = 55

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