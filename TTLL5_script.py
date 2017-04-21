#extracting ClinVar variants from json
#ClinVarVariant:

import json
import objectpath

with open('TTLL5.json') as json_data:
    d = json.load(json_data)
    tree = objectpath.Tree(d)
    for x in (tuple(tree.execute('$..sub'))):
        if str(x).startswith('ClinVarVariant'): print(x)
    raise Exception('jk')

for ClinVar in json_data.find():
    if 'ClinVarVariant' in ClinVar:
        print (ClinVar['ClinVarVariant'])
