liczby = [1,4,6,8,3,7]

liczyDoPotegiDrugiej = []

for liczba in liczby:
    liczyDoPotegiDrugiej.append(liczba**2)


liczbyParzyste = []
for liczba in liczby:
    if(liczba % 2 == 0):
        liczbyParzyste.append(liczba)

# print(liczyDoPotegiDrugiej)
# print(liczbyParzyste)

#poniżej wyrażenie listowne

potegiLiczby2 = [element**2 for element in liczby]
liczbyParzyste2 = [
    liczba  for liczba in liczby if(liczba % 2 == 0)
]
print('potegi2', potegiLiczby2)
print('parzyste', liczbyParzyste2)