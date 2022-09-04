import os

print(os.getcwd()) #pokazuje obecny folder

#os.chdir("../") #zmienia folder
#print(os.getcwd())

print(os.listdir()) #zwraca listę plików obecnego katalogu

print(os.getenv("TMP")) #zwraca zmienną środowiskową

#os.mkdir("folder") #tworzy folder
#os.makedirs("czlonek/stach") #tworzy zagnieżdżone foldery
print(os.listdir())

#os.rmdir("folder") #usuwa folder
#os.removedirs(""czlonek/stach"") #usuwa zagnieżdżone foldery
print(os.listdir())

#os.rename("sample.txt", "sample_new.txt") #zmienia nazwy plików/folderów
#os.renames("sample_new.txt", "sample1.txt") #zmienia nazwy zagnieżdżonych plików/folderów
print(os.listdir())

print(os.stat("data.bin")) #zwraca podstawowe informacje o pliku/folderze

for dirpath, dirnames, filenames in os.walk("C:/Users/khaot/Desktop"): #wędruje po wszystkich podfolderach i zbiera nazwy foderów i plików
    print("Current folder: ", dirpath)
    print("Dictionaries: ", dirnames)
    print("Files: ", filenames)
    print()

print(os.path.isfile("Sample")) #sprawdza czy jest to plik
print(os.path.isdir("Sample")) #sprawdza czy jest to folder
print(os.path.abspath("Sample")) #zwraca sciężkę absotlutną
print(os.path.isabs("Sample")) #sprawdza czy śćieżka jest absolutną
print(os.path.exists("C:/Users/khaot/PycharmProjects/pythonProject/data.bin")) #sprawdza czy istnieje plik/folder
print(os.path.basename("C:/Users/khaot/PycharmProjects/pythonProject/data.bin")) #zwraca nazwę pliku ze scieżki
print(os.path.dirname("C:/Users/khaot/PycharmProjects/pythonProject/data.bin")) #zwraca ścieżkę folderu z pliku
print(os.path.split("C:/Users/khaot/PycharmProjects/pythonProject/data.bin")) #zwraca tuplę ścieżki i pliku
print(os.path.splitext("C:/Users/khaot/PycharmProjects/pythonProject/data.bin")) #zwraca tuplę ścieżki i rozszerzenia pliku