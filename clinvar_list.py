#! /bin/env python
#! /bin/env python
from __future__ import print_function
import sys
import json

clinvar=[]

for l in sys.stdin:
    d=json.loads(l.strip())
    clinvar+=d['clinvar'].keys()

clinvar=list(set(clinvar))

for c in clinvar:
    print(c.encode('utf-8').strip() )


