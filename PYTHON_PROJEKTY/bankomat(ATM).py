print("Witaj")

saldo = 1000

włóż_kartę = input("Włóż kartę")
# wciśnij "enter"

print("Wybierz język:")

lista = ["polski  naciśnij 0", "english naciśnij 1", "deutsch naciśnij 2"]
print(lista[0])
print(lista[1])
print(lista[2])

język = input()

print("Podaj PIN")
#poprawny_pin = 1234

pin = input()
pin = int(pin)
if pin == 1234:
    print("Poprawny PIN")

counter = 1

while pin != 1234:
    print("Niepoprawny PIN")
    print("Podaj PIN")
    print("Jeśli chcesz zakończyć wpisz ANULUJ")
    counter = counter + 1

    pin = input()
    if (pin == "ANULUJ"):
        exit()
    pin = int(pin)

    if (counter == 3 and pin != 1234):
        exit()


    if pin == 1234:
        print("Poprawny PIN")

    continue


#Koniec akcji niepoprawny pin

opcje = ["STAN KONTA      wybierz 0", "WYPŁATA GOTÓWKI wybierz 1"]
print(opcje[0])
print(opcje[1])

opcja = input()
opcja = int(opcja)

if opcja == 0:

    print("")

    print("Twoje saldo wynosi " + str(1000) + " zł")

    print("")


    lista3 = ["Wydruk stanu konta wybierz 0", "Wypłata gotówki wybierz 1", "Zakończ transakcję wybierz 2"]
    print(lista3[0])
    print(lista3[1])
    print(lista3[2])

    lista3 = input()
    lista3 = int(lista3)


    if lista3 == 0:
        print("Drukowanie potwierdzenia")
        print("Proszę odebrać kartę")
        print("Dziękujemy")
        print("Zapraszamy ponownie")
        
    input()
    exit()


    if lista3 == 1:
        print("Proszę czekać...")

    elif lista3 == 2:
        print("Dziękujemy")
        print("Zapraszamy ponownie")
        
    input()
    exit()

# KONIEC akcji STAN KONTA
elif opcja == 1:
    print("Proszę czekać...")

#Tu się zaczyna akcja wyboru kwoty

print("Proszę wybrać kwotę:")

kwota = ["50zł  wciśnij 0", "100zł wciśnij 1", "200zł wciśnij 2", "500zł wciśnij 3", "inna kwota wciśnij 4"]
print(kwota[0])
print(kwota[1])
print(kwota[2])
print(kwota[3])
print(kwota[4])
wybrana_kwota = input()
wybrana_kwota = int(wybrana_kwota)


#zrobic pętle
if wybrana_kwota == 0 or wybrana_kwota == 1 or wybrana_kwota == 2 or wybrana_kwota == 3:
    if wybrana_kwota == 0:
        if (saldo < 50):
            print("Brak środków na koncie")
            print("Sprawdź STAN KONTA")
        else:
            print("Wybrana kwota jest poprawna")
            saldo = saldo - 50
    elif wybrana_kwota == 1:
        if (saldo < 100):
            print("Brak środków na koncie")
            print("Sprawdź STAN KONTA")
        else:
            print("Wybrana kwota jest poprawna")
            saldo = saldo - 100
    elif wybrana_kwota == 2:
        if (saldo < 200):
            print("Brak środków na koncie")
            print("Sprawdź STAN KONTA")
        else:
            print("Wybrana kwota jest poprawna")
            saldo = saldo - 200
    elif wybrana_kwota == 3:
        if (saldo < 500):
            print("Brak środków na koncie")
            print("Sprawdź STAN KONTA")
        else:
            print("Wybrana kwota jest poprawna")
            saldo = saldo - 500
#koniec pętli.żeby po brak srodków, odesłało do stanu konta

if wybrana_kwota == 4:
    print("Podaj kwotę")
    inna = input()
    innaTxt = inna
    inna = int(inna)


    counter = 1

    while (inna > saldo or inna < 10) or (not innaTxt.endswith('0')):
        print("Wybrana kwota jest błędna")
        print("Proszę podać inną kwotę.")
        print("Jeśli chcesz zakończyć wpisz ANULUJ")
        counter = counter +1

        inna = input()
        if (inna == "ANULUJ"):
            exit()

        innaTxt = inna
        inna = int(inna)
        if (counter == 3 and inna > saldo or inna < 10):
            print("Transakcja zostanie zakończona")
            print("Spróbuj ponownie")
            exit()

        if (inna <= saldo and inna >= 10) and (innaTxt.endswith('0')):
            print("Wybrana kwota jest poprawna")


        continue


print("Czy chcesz potwierdzenie transakcji")

potwierdzenie = ["TAK wybierz 0", "NIE wybierz 1"]
print(potwierdzenie[0])
print(potwierdzenie[1])

druk =  input()
druk = int(druk)
if druk == 0:
    print("Drukowanie potwierdzenia")
    print("Proszę odebrać kartę")
    print("Proszę odebrać pieniądze i potwierdzenie")
    print("Dziękujemy")
    print("Zapraszamy ponownie")
if druk == 1:
    print("Proszę odebrać kartę")
    print("Proszę odebrać pieniądze")
    print("Dziękujemy")
    print("Zapraszamy ponownie")

input()
exit()

