from __future__ import print_function
import pymongo
count=0
conn = pymongo.MongoClient(host='*********.cs.ucl.ac.uk', port=*****)
db=conn['u****']

genes=db.genes.find()

for g in genes:
    gene_name=g['gene_name_upper']
    ensembl=g['gene_id']
    variants=db.variants.find({'genes':ensembl})
    cadd_20_count=0
    total_count=0
    for x in variants:
        total_count=total_count+1
        if 'canonical_cadd' in x and x['canonical_cadd'][0]>20:
            cadd_20_count=cadd_20_count+1
    print (gene_name, total_count, cadd_20_count)
