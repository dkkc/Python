# TYPY ZAGNIEŻDZONE 

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"


osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')
 
listaGosci = {
                ('Arkadiusz', 28, 'mężczyzna', 666666666),
                ('Wioletta', 22, 'kobieta', 7777777777),
                ('Kuba', 32, 'mężczyzna', 888888888)  
             }
listaGosci2 = {
                ('Arkadiusz', 28, 'mężczyzna'),
                ('W', 22, 'kobieta'),
                ('K', 32, 'mężczyzna')  
             }

listaZagniezdzona = [('Arkadiusz', 29, 'mężczyzna'), ('Wioletta', 23, 'kobieta'), ('Kuba', 33, 'mężczyzna'),
                     ('Dariusz', 43, 'mężczyzna')]

for name,age,gender,phone in listaGosci:
    print("Imię: ", name)
    print("Wiek: ", age)
    print("Płeć: ", gender)
    print("Tel: ", phone)
    print("\n")

listaGosci3 = listaGosci

print(listaGosci3)





