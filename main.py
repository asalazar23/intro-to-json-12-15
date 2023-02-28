import json 

with open('states.json') as f:
  data = json.load(f)

for state in data['states']:
  # print(state['name'], state['abbreviation'])
  print(state)