#BANK

def stworz_konto():
    imie = str("Podaj imie: ")
    nazwisko = str("Podaj nazwisko: ")
    stan_konta = 0
    dane = [imie, nazwisko, stan_konta]
    baza = open("Konta.txt","r")
    baza.write(dane)
    baza.close()

stworz_konto()










