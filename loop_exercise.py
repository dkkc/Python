serchedNumber = 55
searchingNumber = 0
i = 1

while searchingNumber != serchedNumber:
    searchingNumber = int(input("Zgadnij liczbę: "))
    if(searchingNumber > serchedNumber):
        print("Podana liczba jest większa od liczby szukanej")
    elif(searchingNumber < serchedNumber):
        print("Podana liczba jest mniejsza od szukanej")
    else:
        print("Brawo! Szukana liczba to ", searchingNumber)
  

