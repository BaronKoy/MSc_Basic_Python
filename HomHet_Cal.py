#Obtain average AC and AF
#count homologous and heterozygous

from __future__ import print_function
import sys

adds=0
adds2=0
varnum=0
homcount=0
hetcount=0
for l in sys.stdin:
    d=l.strip()
    #print (d) #for raw data

    if not d.startswith('X'):
        continue
    d=d.split()
    dhomhet=d[9].split(':')
    print (dhomhet)
    if '1/1' in dhomhet[0]:
        homcount=homcount+1
    if '0/1' in dhomhet[0]:
        hetcount=hetcount+1
    for line in d:
        if not line.startswith('AC'):
            continue
        line=line.split(';')
        count=line[0]
        try:
            count2=line[1]
        except:
            continue
        x=count.split('=')
        x2=count2.split('=')
        try:
            xx=x[1]
        except:
            continue
        try:
            xx2=x2[1]
        except:
            continue
        if ',' in xx and ',' in xx2:
            continue
        varnum=varnum+1
        xx=float(xx)
        xx2=float(xx2)
        adds=adds+xx
        adds2=adds2+xx2
avgeAC=adds/varnum
avgeAF=adds2/varnum

print ('Average allele count =',avgeAC)
print ('Average allele frequency =',avgeAF)
print ('Homozygous count =', homcount)
print ('Heterozygous count =', hetcount)
