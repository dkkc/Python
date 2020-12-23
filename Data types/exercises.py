defDictionary = {}

while (True):
    menu = print("Menu\n\r1 - dodaj do słownika\n2 - szukaj w słowniku\n3 - usuń ze słownika\n4 - zakończ program")
    choise = input('Co chcesz zrobić? ')

    if (choise == "1"):
        key = input("Podaj klucz ")
        descr = input("Podaj definicję ")
        defDictionary[key] = descr;
        print("Definicja dodana poprawna")
    elif (choise == "2"):
        key = input("Czego szukasz? ")
        if key in defDictionary:
            print(defDictionary[key])
        else:
            print("definicja nie znaleziona")
    elif (choise == "3"):
        key = input("Co? ")
        if key in defDictionary:
            del defDictionary[key]
            print("Usunięto definicję", key)
        else:
            print("definicja nie znaleziona")
    elif (choise == "4"):
        print("Kończymy program")
        break
    else:
        print("Wybóe poza zakresem")

print(defDictionary)
