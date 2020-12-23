user = {
    'name': "Dariusz",
    'lastName': 'Kowalec',
    'street': 'Staszica',
    'nr': 18,
    'zip-code': '95-010',
    'isBoolean': False,
}

user['zawód'] = 'Programista'
user.update({'age': 43, 'hobby': 'fotografia'})
del(user['isBoolean'])
# delUserProp = user.pop('zawód') # pop usuwa i zwraca usuniętą wartość
# delLastValue = user.popitem() # usuwa ostatni element i zwraca warość


# print('usunięta wartość: ', delUserProp)
# print('usunięta ostatnia wartość: ', delLastValue)
print(user['name'])
print(user);
print(user.get('age'));
print(len(user)); # długość słownika
# user.clear() # czyści zawartość słownika

print(user);

