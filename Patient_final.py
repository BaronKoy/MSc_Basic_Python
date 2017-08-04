from __future__ import print_function
import pymongo
import sys
import re

conn = pymongo.MongoClient(host='*********.cs.ucl.ac.uk', port=*****)
db=conn['ucl**']

adds=0
adds2=0
varnum=0
homcount=0
hetcount=0

count_FIN=float(0)
count_AMR=float(0)
count_AFR=float(0)
count_OTH=float(0)
count_EAS=float(0)
count_ASJ=float(0)
count_NFE=float(0)

for e in sys.stdin:
    data=e.strip()
    data=data.split()
    data=data[0:5]
    del data[2:3]
    data='-'.join(data)
    out=db.ethnicity.find_one({'variant_id':data})
    if out:
        out=out['ethnicity']
        if 'FIN' in out:
                count_FIN=count_FIN+1
        elif 'AMR' in out:
                count_AMR=count_AMR+1
        elif 'AFR' in out:
                count_AFR=count_AFR+1
        elif 'OTH' in out:
                count_OTH=count_OTH+1
        elif 'EAS' in out:
                count_EAS=count_EAS+1
        elif 'ASJ' in out:
                count_ASJ=count_ASJ+1
        elif 'NFE' in out:
                count_NFE=count_NFE+1
    e=e.strip()
    #print (e) #for raw data
    if e.startswith('15'):
        if 'rs1129038' in e:
            d=e.split()
            d=d[9]
            if d.startswith('0/0'):
                print ('         ')
                print ('Predicted eye colour')
                 print ('rs1129038 homozygous reference = Brown/Hazel eyes')
            elif d.startswith('0/1'):
                print ('         ')
                print ('Predicted eye colour')
                print ('rs1129038 heterozygous = Brown/Hazel eyes')
            elif d.startswith('1/1'):
                print ('         ')
                print ('Predicted eye colour')
                print ('rs1129038  homozygous alterantive = Blue/Grey/Green eyes')
            else:
                print ('Variant not found')
    elif e.startswith('X'):
        g=e.strip()
        g=g.split()
        ghomhet=g[9].split(':')
        if '1/1' in ghomhet[0]:
            homcount=homcount+1
        if '0/1' in ghomhet[0]:
            hetcount=hetcount+1
        for line in g:
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

print ('         ')
print ('Gender prediction')
print ('Average X allele count =',avgeAC)
print ('Average X allele frequency =',avgeAF)
print ('Homozygous X count =', homcount)
print ('Heterozygous X count =', hetcount)

if homcount>hetcount:
    print ('Homozygous X = Male')
else:
    print ('Heterozygous X = Female')

FIN_percent=(count_FIN/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
AMR_percent=(count_AMR/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
AFR_percent=(count_AFR/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
OTH_percent=(count_OTH/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
EAS_percent=(count_EAS/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
ASJ_percent=(count_ASJ/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
NFE_percent=(count_NFE/(count_FIN+count_AMR+count_AFR+count_OTH+count_EAS+count_ASJ+count_NFE))*100
print ('           ')
print ('Ethnicity prediction')
print ('Finnish SNPs =',FIN_percent,'%')
print ('Latino SNPs =',AMR_percent,'%')
print ('African SNPs =',AFR_percent,'%')
print ('Other ethnicity SNPs =',OTH_percent,'%')
print ('East Asian SNPs =',EAS_percent,'%')
print ('Ashkenazi Jewish SNPs =',ASJ_percent,'%')
print ('European SNPs =',NFE_percent,'%')
final_count=max(count_FIN,count_AMR,count_AFR,count_OTH,count_EAS,count_ASJ,count_NFE)
if final_count==count_FIN:
        print ('Predicted ethnicity = Finnish')
elif final_count==count_AMR:
        print ('Predicted ethnicity = Latino')
elif final_count==count_AFR:
         print ('Predicted ethnicity = African')
elif final_count==count_OTH:
        print ('Predicted ethnicity = Other ethnicity')
elif final_count==count_EAS:
        print ('Predicted ethnicity = East Asian')
elif final_count==count_ASJ:
        print ('Predicted ethnicity = Ashkenazi Jewish')
elif final_count==count_NFE:
        print ('Predicted ethnicity = European')




