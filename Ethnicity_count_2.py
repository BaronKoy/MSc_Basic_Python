#Similar to ethnicity_1 but removes unwanted information
#Adds the average frequency of ethnicity variants across the genome

#Packages
from __future__ import print_function
import json
import re
import sys
import operator

#Keys
#FIN: Finnish
#AMR: Latino
#AFR: African/African American
#OTH: Other
#EAS: East Asian
#ASJ: Ashkenazi Jewish
#NFE: Non-Finnish European
#raw: raw count
#Female: Female count
#Male: Male count

total=dict()
figs=dict()
extra=dict()

count_FIN=0
count_AMR=0
count_AFR=0
count_OTH=0
count_raw=0
count_EAS=0
count_ASJ=0
count_NFE=0
count_Female=0
count_Male=0
count_process=0


for data in sys.stdin:
    data=data.strip()
    data=json.loads(data)
    chromo=data['strand']
    locat=data['start']
    alle=data['allele_string']
    if not 'custom_annotations' in data:
         continue
    if not 'gnomad_genomes' in data['custom_annotations']:
         continue
    nomad=data['custom_annotations']['gnomad_genomes']
    for r in nomad:
         nums=r['fields']
         figs={'AF_FIN': nums['AF_FIN'],'AF_AMR': nums['AF_AMR'],'AF_AFR': nums['AF_AFR'],
         'AF_OTH': nums['AF_OTH'], 'AF_EAS': nums['AF_EAS'],'AF_ASJ': nums['AF_ASJ'],
         'AF_NFE':nums['AF_NFE']}
         extra={'AF_raw': nums['AF_raw'],'AF_Female': nums['AF_Female'],'AF_Male': nums['AF_Male']}
         sorted_figs=sorted(figs.items(), key=operator.itemgetter(1),reverse=True)
         try:
             count_FIN=count_FIN+nums['AF_FIN']
             count_AMR=count_AMR+nums['AF_AMR']
             count_AFR=count_AFR+nums['AF_AFR']
             count_OTH=count_OTH+nums['AF_OTH']
             count_raw=count_raw+nums['AF_raw']
             count_EAS=count_EAS+nums['AF_EAS']
             count_ASJ=count_ASJ+nums['AF_ASJ']
             count_NFE=count_NFE+nums['AF_NFE']
             count_Female=count_Female+nums['AF_Female']
             count_Male=count_Male+nums['AF_Male']
             count_process=count_process+1
          except:
             continue
         predict=max(figs,key=figs.get)
         if predict==0:
             continue
         print ('Variant_I.D:',chromo,locat,alle)
         print (sorted_figs)
         print ('Predicted_ethnicity:',predict)
print('Finnish_average_count:',count_FIN/count_process)
print('Latino_average_count:',count_AMR/count_process)
print('African_average_count:',count_AFR/count_process)
print('EastAsian_average_count:',count_EAS/count_process)
print('AshKenJewish_average_count:',count_ASJ/count_process)
print('NonFinEuro_average_count:',count_NFE/count_process)
print('OTH_average_count:',count_OTH/count_process)
