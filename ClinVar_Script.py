from __future__ import print_function
import json
import objectpath
import requests
import urllib

with open('TTLL5.json') as json_data:
    d = json.load(json_data)
    tree = objectpath.Tree(d)
    for x in (tuple(tree.execute('$..sub'))):
        if str(x).startswith('ClinVarVariant'): print(x)

for ClinVar in json_data.find():
    if 'ClinVarVariant' in ClinVar:
        print (ClinVar['ClinVarVariant'])

url='https://www.ncbi.nlm.nih.gov/clinvar/variation/139517/'.format(y)
r=requests.get('https://www.ncbi.nlm.nih.gov/clinvar/variation/139517/')
print (r)
