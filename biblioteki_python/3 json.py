import json

'''
json.loads() #ładoawnie json ze stringa
json.load()  #ładowanie jsona z pliku
json.dump()  #wkładanie jsona do pliku
json.dumps() #wkładnie jsona do stringa
'''

with open('states.json', 'r') as f:
    data = json.load(f)

for i in data['states']:
    del i['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)