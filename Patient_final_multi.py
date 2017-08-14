from __future__ import print_function
from collections import Counter
import pymongo
import sys
import re
import json

conn = pymongo.MongoClient(host='phenotips')
db=conn['uclex']

varlist=list()
ethlist=list()
genelist=list()
homcount=0
hetcount=0

fields=['CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT']

samples=[]
data=dict()

for l in sys.stdin:
    if l.startswith('##'): continue
    if l.startswith('#CHROM'):
        l=l.replace('#','')
        header=l.strip().split()
        samples=list(set(header)-set(fields))
        for s in samples:
            data[s]={
                    'cadd>20':list(),
                    'clinvar':list(),
                    'ethnicity':dict(),
                    'miss_count':0,
                    'het_count':0,
                    'hom_count':0,
                    'wt_count':0,
                    'x_hom_count':0,
                    'x_het_count':0
                    }
        continue
    d=l.strip().split()
    d=dict(zip(header,d))
    variant_id='-'.join([d[x] for x in ('CHROM','POS','REF','ALT')])
    # lookup variant in variant store
    var=db.variants.find_one({'variant_id':variant_id})
    eth=db.ethnicity.find_one({'variant_id':variant_id})
    clin=db.clinvar.find_one({'variant_id':variant_id})
    for s in samples:
        x=d[s]
        if x.startswith('./.'):
            data[s]['miss_count']+=1
        elif x.startswith('0/0'):
            data[s]['wt_count']+=1
        elif x.startswith('0/1'):
            data[s]['het_count']+=1
        elif x.startswith('1/1'):
            data[s]['hom_count']+=1
        # eye colour variant 15-28356859-C-T
        if variant_id=='15-28356859-C-T':
            if x.startswith('1/1'):
                data[s]['eye_colour']='blue'
            else:
                data[s]['eye_colour']='brown'
        if variant_id.startswith('X'):
            if x.startswith('1/1'):
               data[s]['x_hom_count']+=1
            elif x.startswith('0/1'):
               data[s]['x_het_count']+=1
        if x.startswith('0/1') or x.startswith('1/1'):
            if var and 'canonical_cadd' in var and var['canonical_cadd'][0]>20:
                data[s]['cadd>20']+=[var['canonical_gene_name_upper'][0]]
            if clin:
                data[s]['clinvar']+=[clin]
            if eth:
                eth['ethnicity']=eth['ethnicity'].replace('AF_','')
                data[s]['ethnicity'][eth['ethnicity']]=data[s]['ethnicity'].get(eth['ethnicity'],0)+1


for s in samples:
    x=data[s]
    ethnicities=[e for e in x['ethnicity']]
    out=dict()
    out['sample']=s
    out['miss_count']=x['miss_count']
    out['wt_count']=x['wt_count']
    out['het_count']=x['het_count']
    out['hom_count']=x['hom_count']
    out['x_hom_count']=x['x_hom_count']
    out['x_het_count']=x['x_het_count']
    if out['x_hom_count']==0 or x['x_het_count']==0:
        out['gender']='U'
    elif out['x_hom_count']>2*x['x_het_count']:
        out['gender']='F'
    else:
        out['gender']='M'
    out['clinvar']=dict(Counter([ v['phenotypes'][0] for v in x['clinvar']]))
    out['cadd>20']=dict(Counter( x['cadd>20'] ))
    out['ethnicity']={e:x['ethnicity'][e] for e in ethnicities}
    if 'eye_colour' in x: out['eye_colour']=x['eye_colour']
    print(json.dumps(out))


