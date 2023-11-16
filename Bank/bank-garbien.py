#BANK

def stworz_konto():
    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    stan_konta = str(input("Podaj poczontkowy stan konta: "))
    dane = [imie, nazwisko, stan_konta]
    baza = open("Konta.txt","a")

    baza.write(imie)
    baza.write(nazwisko)
    baza.write(stan_konta)
    
    baza.close()
    print("Stworzono konto", *dane)
stworz_konto()










