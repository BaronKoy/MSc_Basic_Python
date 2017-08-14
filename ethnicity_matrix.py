#! /bin/env python
from __future__ import print_function
import sys
import json

ethnicities=[]
data=dict()

for l in sys.stdin:
    d=json.loads(l.strip())
    ethnicities+=d['ethnicity'].keys()
    s=d['sample']
    if s not in data:
        data[s]=dict()
    data[s]['ethnicity']=d['ethnicity']
    data[s]['het_count']=d['het_count']
    data[s]['hom_count']=d['hom_count']
    data[s]['eye_colour']=d['eye_colour']

ethnicities=list(set(ethnicities))

print('sample,'+','.join(ethnicities)+',het_count,hom_count,eye_colour')
for s in data:
    x=data[s]
    print(s, ','.join([str(x['ethnicity'].get(e,0)) for e in ethnicities]), x['het_count'], x['hom_count'],x['eye_colour'],sep=',')



