'''
listy - mutowalna sekwencje, które przechowują różne typy danych,
można dostać się po indeksie do danych elementów

tuple - niemutowalne sekwancje, które przechowują różne typy danych,
można dostać się po indeksie do danych elementów

słowniki - mutowalne sekewencje, które są inaczej nazywane mapą 
lub tablicą asociacyjną ponieważ do elementów dostajemy się po 
unikalnych wartościach zawnymi kluczami

sety - mutowalne sekwencje, które posiadają unikalne elementy,
a więc żaden element nie może się powtarzać w sekwencji
'''

#listy
list_ = [1, 2, 3, 4, 5]
for i in list_:
    print(i)


#tuple
tuple_ = (1, 2, 2, 3, 4, 5)
print(tuple_)
print(tuple_.count(2))
print(tuple_[-1])


#słowniki
dict_ = {
    'north' : 'północ',
    'south' : 'południe',
    'west' : 'zachód',
    'east' : 'wschód',
    1 : [1, 2, 3, 4]
}

print(dict_.keys())
print(dict_.values())


for val, key in dict_.items():
    print(val, key, sep=" - ")

print(dict_['north'])


#sety
set_ = set([1, 2, 3, 4, 5])
print(set_)
set_.add(2)
print(set_)


'''
comprehension - sposób szybkiego deklarowania sekewencyjnych
typów z danymi wartościami
można tak deklarować: listy, sety, tuple(lekko naciągane) i słowniki
'''

#listy
list_c = [i*i for i in range(1, 11) if i % 2 == 0]
print(list_c)

#sety
set_c = {i for i in range(1, 11)}
print(set_c)

#słowniki
dict_c = {i : i ** 2 for i in range(1, 11) if i % 2 == 0}
print(dict_c)

#tuple nie są 'comprehension', za to jest zwracany obiekt generatora,
#który możemy rozpakować
tuple_c = (i for i in range(1, 6))
print(*tuple_c)

#operator * służy do rozpakowywania typów sekwencyjnych