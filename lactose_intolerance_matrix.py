#! /bin/env python

#! /bin/env python
from __future__ import print_function
import sys
import json

data=dict()

for l in sys.stdin:
    d=json.loads(l.strip())
    data[d['sample']]=d['clinvar'].get('Lactose intolerance',0)

print('sample,lactose_intolerance')
for s in data:
    print(s, data[s], sep=',')


