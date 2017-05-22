'''Obtaining elements from variant json files
updated: 15/05/2017'''


#packages
from __future__ import print_function
import json
import subprocess
import objectpath

#Python Bionode Search (substitute variant id accordingly)
a=subprocess.check_output(['bionode-ncbi', 'search', 'clinvar', '139517'])
b=json.loads(a)

#Obtaining targeted elements
c=b['variation_set'][0]['variation_loc'][1]
d=b['genes'][0]
e=b['variation_set'][0]
f=b['trait_set'][0]

c['assembly_name'],d['symbol'],b['uid'],c['band'],c['display_start'],c['stop'],d['strand'],c['ref'],c['alt'],e['variant_type'],f['trait_name']
