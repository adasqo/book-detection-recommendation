"""
Dla kazdego wykrytego slowa, wykryj jego sasiadow. 
"""


import json

data = None
with open('test.json') as json_file:
    data = json.load(json_file)

for details in data.values():
    print(details)