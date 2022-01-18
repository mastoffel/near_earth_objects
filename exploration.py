import csv
import importlib
import json

with open('data/neos.csv', 'r') as f:
    csv_reader =  csv.reader(f)
    named_rows = [row for row in csv_reader if row[15] != '']

len(named_rows)
named_rows[0]

with open('data/cad.json', 'r') as f:
    json_reader = json.load(f)

json_reader['count']
    
json_reader['fields']
[entry for entry in json_reader['data'] if ('2000-Jan-01' in entry[3]) and ('2002 PB' in entry[0])]


import extract
import database
import importlib
import models
importlib.reload(extract)
importlib.reload(database)
importlib.reload(models)
approaches = extract.load_approaches('data/cad.json')
neos = extract.load_neos('data/neos.csv')
neodb = database.NEODatabase(neos, approaches)

neodb.get_neo_by_name('Pimentel')
approaches_dict = {}
for approach in approaches:
            if not approach._designation in approaches_dict.keys():
                approaches_dict[approach._designation] = [approach]
            else:
                approaches_dict[approach._designation].append(approach)

neos_dict = {}
for neo in neos:
            if not neo.designation in neos_dict.keys():
                neos_dict[neo.designation] = [neo]
            else:
                neos_dict[neo.designation].append(neo)
                
def counter(num):
    for i in range(5):
        if i > 2:
            yield print(i)
            
next(counter(2))

def approach_gen(approaches):
    for approach in approaches[0:10]:
        yield approach
            
iter(approach_gen(approaches))

mydict = {'lol': 10,
          'hey': 11}
mydict