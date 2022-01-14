import csv
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

