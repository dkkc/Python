'''
Funkcje, które pomogą operować na listach :

len() - (z ang length) czyli długość, ilość elementów w liście np.

    print(len(lista1))


 append - dodawanie jednego elementu do końca listy np.

    lista1.append(4)
    print(lista1)

extend - rozszerzenie listy o nową liste np.

    lista1.extend([2,6,5,8])
    print(lista1)

insert - z ang. wstawić element wewnątrz listy np. na pozycji 1 wstawimy 'Kuba'

    lista2.insert(1,"Kuba")
    print(lista2)


index - pozwoli nam otrzymać index szukanego elementu. Należy pamiętać, że indeks zwraca nam pierwsze wystąpienie elementu np.
jeśli w liście lista1 = [66,31,5,47,66,12] element 66 jest na pozycji 0 jak również na pozycji 4 , zostanie podany jego pierwszy indeks tj. 0

    print(lista1.index(66))


sort - funkcja, która pozwala posortować elementy rosnąco lub malejąco. Całkowicie zmienia oryginalną zawartość. Standardowe sortowanie to sortowanie rosnące. Gdy prześlemy zmienną reverse=True (z ang. reverse - na odwrót) sortowanie będzie malejące.


max - wyszukanie maksymalnej wartości w liście np.

   print(max(lista1))


min - wyszukanie najmniejszej wartości w liście np.

       print(min(lista1))


count - pozwala policzyć, ile razy dany element wystąpił w liście np.

        print(lista1.count(66))


pop -  usuwa ostatni element z listy np.

    lista1.pop()

remove - usunięcie pierwszego wystąpienia np.

        lista1.remove(1)

clear - czyszczenie listy, usunięcie wszystkich elementów np.

        lista1.clear()
     print(lista1)

reverse - zmiana kolejności elementów, na odwrót niż oryginalnie np.

      lista1 = [66,31,5,47,66,12]
      lista1.reverse()
      print(lista1)
      Wydrukuje nam liste w zmienionej kolejności tj. [12,66,47,5,31,66]
'''
numList = [1, 2, -4, -5, 40, 55, -100, 'Dariusz']
numList.extend(['Mateusz'])
numList.insert(3, 33)

if('Dariusz' in numList):
    print('In')
else:
    print('not in')

print('index', numList.index("Mateusz"))
print(len(numList));
print(numList);

