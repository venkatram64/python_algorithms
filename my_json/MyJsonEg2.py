import json

with open('states.json') as f:
    data = json.load(f)
    print(data)

for state in data['states']:
    print(state)

for state in data['states']:
    print(state['name'], state['abbreviation'])

#deleting area code from json
for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)