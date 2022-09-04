import pickle
#moduł pozwala na sterylizacje danych do postaci bitowej i łatwo zamienia dane w obie strony

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#zapisanie danych bitowych do plicku
file = open("data.bin", "wb")
file.write(pickle.dumps(data))
file.close()

#odczytanie danych bitowych z pliku
file = open("data.bin", "rb")
print(pickle.loads(file.read()), "ładowanie danych")
file.close()

#zamienne metody
file = open("data.bin", "wb")
pickle.dump(data, file)
file.close()

file = open("data.bin", "rb")
print(pickle.load(file), "ładowanie danych 2")
file.close()