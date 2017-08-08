from __future__ import print_function
import sys
import json
import collections

for data in sys.stdin:
    var=data.strip()
    var=var.split()
    var=var[0:5]
    del var[2:3]
    var='-'.join(var)
    adict={'Variant':var}

    dbn=data.strip()
    dbn=dbn.split()
    dbn=dbn[7:8]
    dbn=''.join(dbn)
    dbn=dbn.split(';')
    for line in dbn:
        if 'CLNDBN' in line:
            clndbn=line
            clndbn=clndbn.split('=')
            clndbn=''.join(clndbn)
            clndbn=clndbn.split('|')
            clndbn=' - '.join(clndbn)
            bdict={clndbn[0:6]:clndbn[6:]}

        if 'CLNREVSTAT' in line:
            revstat=line
            revstat=revstat.split('=')
            revstat=''.join(revstat)
            revstat=revstat.split('|')
            revstat='-'.join(revstat)
            cdict={revstat[0:10]:revstat[10:]}

        if 'CLNACC' in line:
            acc=line
            acc=acc.split('=')
            acc=''.join(acc)
            acc=acc.split('|')
            acc='-'.join(acc)
            ddict={acc[0:5]:acc[5:]}
            jdict=dict(adict, **bdict)
            jdict.update(cdict)
            jdict.update(ddict)
            jdict.update(edict)
            print (jdict)

        if 'CLNSIG' in line:
            sig=line
            sig=sig.split('=')
            sig=''.join(sig)
            sig=sig.split('|')
            sig='-'.join(sig)
            edict={sig[0:6]:sig[6:]}
