'''choise = input("1-monożeni, 2 - dzielenie, 3-odejmowanie, 4 - dodawanie:")

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if(int(choise) == 1):
    print(num1 * num2)
elif (int(choise) == 2 ):
    if(num2 == 0):
        print("nie dzielimy przez zero!")
    else:
        print(num1/num2)
elif (int(choise) == 3 ):
    print(num1 - num2)
elif(int(choise) == 4 ):
    print(num1 + num2)
else:
    print("Dupa")'''
import math
    
# intNumber = int(input("podaj liczbę: "))

# print("Liczba całkowita:", int(math.fabs(intNumber)))

'''
OPERATORY LOGICZNE

and,
or,
not

'''
a = int(input("Liczba:"))

if(a == 2 or a > 10 ):
    print(a,"jest w przedziale od 1 do 10")
else:
    print(a," nie jest w przedziale od 1 do 10")
