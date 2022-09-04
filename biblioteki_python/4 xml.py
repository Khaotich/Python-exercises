import xml.etree.ElementTree as et

#wczytanie drzewa xml z pliku
tree = et.parse('hoders.xml')
#uzyskanie roota drzewa, czyli głównego tagu
root = tree.getroot()

#uzyskujemy wartość atrybutu
print(root.get('coin'))

#ustawiamy wartość atrybutu
root.set('launched', '20220714')

#uzyskujemy słownik atrybutów
print(root.attrib)

for i, investor in enumerate(root.findall('investor')):
    investor.set('id', str(i+1))

#usunięcie atrybutów
#for investor in root.findall('investor'):
    #del investor.attrib['id']

#dodanie tagu inwestora
investor = et.Element('investor')
investor.text = 'Khaotic'
root.append(investor)

#uzyskanie tekstu tagu o zadanym atrybucie
investor = root.find('.//investor[@id="4"]')
print(investor.text)

#zapisanie drzewa xml do pliku
tree.write('hoders.xml')