#Packages
from __future__ import print_function
import json
import re
import sys

#Keys
#FIN: Finnish
#AMR: Latino
#AFR: African/African American
#OTH: Other
#raw: raw count
#Female: Female
#EAS: East Asian
#ASJ: Ashkenazi Jewish
#NFE: Non-Finnish European


total=dict()
figs=dict()
count_FIN=0
count_AMR=0
count_AFR=0
count_OTH=0
count_raw=0
count_Female=0
count_EAS=0
count_ASJ=0
count_NFE=0
for  data in sys.stdin:
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
        figs={'AC_FIN': nums['AC_FIN'],'AC_AMR': nums['AC_AMR'],'AC_AFR': nums['AC_AFR'],
        'AC_OTH': nums['AC_OTH'],'AC_raw': nums['AC_raw'],'AC_Female': nums['AC_Female'],
        'AC_EAS': nums['AC_EAS'],'AC_ASJ': nums['AC_ASJ'],'AC_NFE': nums['AC_NFE']}
        count_FIN=count_FIN+nums['AC_FIN']
        count_AMR=count_AMR+nums['AC_AMR']
        count_AFR=count_AFR+nums['AC_AFR']
        count_OTH=count_OTH+nums['AC_OTH']
        count_raw=count_raw+nums['AC_raw']
        count_Female=count_Female+nums['AC_Female']
        count_EAS=count_EAS+nums['AC_EAS']
        count_ASJ=count_ASJ+nums['AC_ASJ']
        count_NFE=count_NFE+nums['AC_NFE']
        print (chromo,locat,alle)
        print (figs)
    print ('FIN_total:',count_FIN,'AMR_total:',count_AMR,'AFR_total:',count_AFR,'OTH_total:',count_OTH,
    'raw_total:',count_raw,'Female_total:',count_Female,'EAS_total:',count_EAS,'ASJ_total:',count_ASJ,
    'NFE_total:',count_NFE)
