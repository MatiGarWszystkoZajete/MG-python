# Hasla
import random
dlugoschasla = 0
haslo = []
if dlugoschasla < 8:
    dlugoschasla = int(input("Wypisz dlugosc hasla (min 8): "))

while dlugoschasla != 0:
    LiteraM = random.choice("qwertyuiopasdfghjklzxcvbnm")
    LiteraD = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
    cyfry = random.choice("1234567890")
    typ = random.randint(0,3)
    if typ == 1:
        typ = LiteraM
    elif typ == 2:
        typ = LiteraD
    elif typ == 3:
        typ = cyfry
    haslo.append(typ)
    dlugoschasla-=1

print("Twoje haslo: ")
print(*haslo, sep="")
