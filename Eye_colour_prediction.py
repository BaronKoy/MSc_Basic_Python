from __future__ import print_function
from pysam import VariantFile
import sys
from collections import Counter

f=VariantFile('*******_April***.vcf.gz')

chrom='1'
start=1
end=100000

s=r.samples
for snps in s:
    if 'rs1129038' in snps:
        print (snps)


horef=0
heref=0
hoalt=0
nopres=0

for l in sys.stdin:
    d=l.strip()
    d=d.split('(')
    for line in d:
        if line.startswith('0, 0'):
            horef=horef+1
        if line.startswith('0, 1'):
            heref=heref+1
        if line.startswith('1, 1'):
            hoalt=hoalt+1
        if line.startswith('None, None'):
            nopres=nopres+1
    print ('Homologous reference count=', horef, 'Blue/Grey/Green eyes')
    print ('Heterozygous count=', heref, 'Brown/Hazel eyes')
    print ('Homologous alternative count=', hoalt, 'Brown/Hazel eyes')
    print ('Not present count=', nopres)
