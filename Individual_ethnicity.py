from __future__ import print_function
import sys

for data in sys.stdin:
    data=data[3:]
    data=data.strip()
    data=data.split('u')
    data=''.join(data)
    print (data)


for data in sys.stdin:
    data=data.strip()
    data=data.split()
    data=data[0:5]
    del data[2:3]
    data='-'.join(data)
    print (data)

with open('ethnicity.txt','r') as data:
    for line in data:
        line=line.strip()
        with open('all_variants.txt','r') as data2:
            for line2 in data2:
                line2=line2.strip()
                if line2 in line:
                    print (line)
    
