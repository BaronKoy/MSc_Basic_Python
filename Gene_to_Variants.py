'''Obtaining ClinVar information from json file created from Biolink API
updated: 18/05/2017'''


#packages
from __future__ import print_function
import json
import objectpath
import requests
import subprocess
import pymongo
import re
import sys

hpo=sys.argv[0]
print (hpo)

#machine holding patient information
conn = pymongo.MongoClient(host='phenotips.cs.ucl.ac.uk', port=27017)

#dictionary that holds all variant and patient information
variants_db=conn['uclex']
patients_db=conn['patients']





args=[
('defType','edismax'),
('qt','standard'),
('indent','on'),
('wt','csv'),
('rows','100000'),
('start','0'),
('fl','subject,subject_label,subject_taxon,subject_taxon_label,subject_gene,subject_gene_label,object,object_label,relation,relation_label,evidence,evidence_label,source,is_defined_by,qualifier'),
('facet','true'),
('facet.mincount','1'),
('facet.sort','count'),
('json.nl','arrarr'),
('facet.limit','25'),
('facet.method','enum'),
('csv.encapsulator','"'),
('csv.separator',','),
('csv.header','true'),
('csv.mv.separator','|'),
('fq','subject_category:"variants"'),
('fq','object_closure:"HP:0000556"'),
('facet.field','subject_taxon_label'),
('q','*:*')]

#'hpo='HP:0000556'
hpo='HP:0007750'
args={
'defType':'edismax',
'qt':'standard',
'indent':'on',
'wt':'csv',
'rows':'100000',
'start':'0',
'fl':'subject,subject_label,subject_taxon,subject_taxon_label,subject_gene,subject_gene_label,object,object_label,relation,relation_label,evidence,evidence_label,source,is_defined_by,qualifier',
'facet':'true',
'facet.mincount':'1',
'facet.sort':'count',
'json.nl':'arrarr',
'facet.limit':'25',
'facet.method':'enum',
'csv.encapsulator':'"',
'csv.separator':',',
'csv.header':'true',
'csv.mv.separator':'|',
#'fq':['subject_category:"variants"','object_closure:"HP:0000556"'],
'fq':'object_closure:"%s"' % hpo,
'facet.field':'subject_taxon_label',
'q':'*:*'}
p=requests.get('http://solr.monarchinitiative.org/solr/golr/select/',params=args)
s=p.text
l=s.split('\n')
for x in l:
    if 'ClinVarVariant' in x:
        xx=x.split(',')[0]
        #print (x)
        x2=xx.split(':')[1]
        a=subprocess.check_output(['bionode-ncbi', 'search', 'clinvar', x2])
        b=json.loads(a)
        gene=';'.join([x['symbol'] for x in b['genes']])
        #Forloop for variation set
        variation_set=b['variation_set']
        for v in variation_set:
            if 'variation_loc' not in v: continue
            for vloc in v['variation_loc']:
                if vloc['assembly_name']!='GRCh37': continue
                var='-'.join([vloc['chr'],vloc['start'],vloc['ref'],vloc['alt']])
                exac=requests.get('http://exac.hms.harvard.edu/rest/variant/'+var)
                if exac.status_code == requests.codes.ok:
                    exac=exac.json()
                    exac_af=exac['variant'].get('allele_freq',None)
                else:
                    exac_af=None
                rec=variants_db.variants.find_one({'variant_id':var})
                if rec: print(var,x2,exac_af,gene,';'.join(rec['het_samples']),';'.join(rec['hom_samples']),sep=',')
                else: print(var,x2,exac_af,gene,'not found', 'not found', sep=',')

