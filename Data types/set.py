"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy          NIE           TAK             TAK                   TAK
krotki         NIE           TAK             NIE                   NIE
słowniki       TAK           NIE             TAK                   TAK
zbiory         TAK           NIE             NIE                   TAK

        ZBIORY: BONUS w postaci | & - ^ 
"""

A = {1, 4, 20, -4, 20}

B = {1, 4}

C = [3,5,6,7,8,8,8,8,9,0,12,13];


print(C)

A.add(45)

print(set(C))
print(A)
print(A.issubset(B))
print(B.issubset(A))
print(A&B) # pokaże wspólne elemnty zbiorów A i B
print(A-B)
print(A|B)
print(A^B) # wyklucz częsci wspólne


