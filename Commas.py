#Script to replace '-' in csv HPO files to comma's.
#Updated 23/05/2017

#packages
import sys

for l in sys.stdin.readlines():
    x=l.strip().split(',')
    x[0]=x[0].replace('-',',')
    print(','.join(x))
