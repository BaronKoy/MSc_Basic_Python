#! /bin/env python
from __future__ import print_function
import sys
import json

genes=[]
data=dict()

for l in sys.stdin:
    d=json.loads(l.strip())
    genes+=d['cadd>20'].keys()
    data[d['sample']]=d['cadd>20']

genes=list(set(genes))

print('sample,'+','.join(genes))
for s in data:
    x=data[s]
    print(s, ','.join([str(x.get(g,0)) for g in genes]), sep=',')


