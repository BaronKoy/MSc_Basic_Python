from __future__ import print_function
import json
import sys

FIN_fig=0
AMR_fig=0
AFR_fig=0
OTH_fig=0
EAS_fig=0
ASJ_fig=0
NFE_fig=0
Final=0
for data in sys.stdin:
    spaces=data.strip()
    words=spaces.split()
    for x in words:
        if 'AF' in x:
            Final=Final+1
     for line in words:
         if 'FIN' in line:
            FIN_fig=FIN_fig+1
         elif 'AMR' in line:
             AMR_fig=AMR_fig+1
         elif 'AFR' in line:
             AFR_fig=AFR_fig+1
         elif 'OTH' in line:
             OTH_fig=OTH_fig+1
         elif 'EAS' in line:
             EAS_fig=EAS_fig+1
         elif 'ASJ' in line:
             ASJ_fig=ASJ_fig+1
         elif 'NFE' in line:
             NFE_fig=NFE_fig+1
         else:
             continue
FIN_p=(float(FIN_fig)/Final)*100
AMR_p=(float(AMR_fig)/Final)*100
AFR_p=(float(AFR_fig)/Final)*100
OTH_p=(float(OTH_fig)/Final)*100
EAS_p=(float(EAS_fig)/Final)*100
ASJ_p=(float(ASJ_fig)/Final)*100
NFE_p=(float(NFE_fig)/Final)*100
print ('Finnish_percentage:',FIN_p,'%')
print ('Latino_percentage:',AMR_p,'%')
print ('African_percentage:',AFR_p,'%')
print ('Other_percentage:',OTH_p,'%')
print ('EastAsian_percentage:',EAS_p,'%')
print ('AshkenaziJewish_percentage:',ASJ_p,'%')
print ('Non-Finnish_Euro_percentage:',NFE_p,'%')
