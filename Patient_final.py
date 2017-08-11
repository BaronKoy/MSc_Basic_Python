from __future__ import print_function
from collections import Counter
import pymongo
import sys
import re

conn = pymongo.MongoClient(host='phenotips')
db=conn['uclex']

varlist=list()
ethlist=list()
genelist=list()
homcount=0
hetcount=0

for e in sys.stdin:
    data=e.strip()
    data=data.split()
    data=data[0:5]
    del data[2:3]
    data='-'.join(data)
    var=db.variants.find_one({'variant_id':data})
    if var and 'canonical_cadd' in var and var['canonical_cadd'][0]>20:
        genelist.append(var['canonical_gene_name_upper'][0])
    clin=db.clinvar.find_one({'Variant':data})
    if clin and clin['CLNDBN']!='not_specified':
        varlist.append(clin['CLNDBN'])
    out=db.ethnicity.find_one({'variant_id':data})
    if out:
        ethlist.append(out['ethnicity'])

    e=e.strip()
    if e.startswith('15'):
        if 'rs1129038' in e:
            d=e.split()
            d=d[9]
            if d.startswith('0/0'):
                print ('         ')
                print ('Predicted eye colour:')
                print ('rs1129038 homozygous reference = Brown/Hazel eyes')
            elif d.startswith('0/1'):
                print ('         ')
                print ('Predicted eye colour:')
                print ('rs1129038 heterozygous = Brown/Hazel eyes')
            elif d.startswith('1/1'):
                print ('         ')
                print ('Predicted eye colour:')
                print ('rs1129038  homozygous alterantive = Blue/Grey/Green eyes')
            else:
                print ('Variant not found')

    if e.startswith('X'):
        g=e.strip()
        g=g.split()
        ghomhet=g[9].split(':')
        if '1/1' in ghomhet[0]:
            homcount=homcount+1
        if '0/1' in ghomhet[0]:
            hetcount=hetcount+1

print ('Gender prediction:')
print ('Homozygous X count =', homcount)
print ('Heterozygous X count =', hetcount)
if homcount>hetcount:
    print ('Homozygous X : Male')
else:
    print ('Heterozygous X : Female')
print (genelist)
print ('Ethnicity counts:',Counter(ethlist))
print ('Disease variants:',Counter(varlist))
