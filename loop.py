'''number = 100

while number >= 0:
    print(number)
    number -= 1 '''

result = 0
i = 0

'''while iteration < 4:
    x = int(input("Podaj liczbę"))
    result += x
    iteration += 1 '''

'''for i in range(0,4):
    x = int(input("Podaj liczbę"))
    result += x '''

'''for i in range(120):
    #x = int(input("Podaj liczbę"))
    if(i % 2 == 0): 
        result += i '''

while i < 3:
    x = int(input("Podaj liczbę dodatnią: "))
    if (x > 0 and x % 2 == 0):
        result += x
    else:
        print("Podana liczba musi być liczbą dodatnią i parzystą")
        continue
    i += 1

print("Wynik: ", result)
