#! /bin/env python
from __future__ import print_function
import sys
#from cElementTree import iterparse
from xml.etree.cElementTree import iterparse
from cStringIO import StringIO
import datetime, time
import gzip
import json


source=gzip.open('ClinVarFullRelease_00-latest.xml.gz','r')

# get an iterable
context = iterparse(source, events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
event, root = context.next()


#<TraitSet Type="Disease">
#<Trait Type="Finding">
#<Name>
#<ElementValue Type="Preferred">HP:0010837</ElementValue>
#</Name>
#</Trait>
#<Trait Type="Finding">
#<Name>
#<ElementValue Type="Preferred">HP:0011967</ElementValue>
#</Name>
#</Trait>
#</TraitSet>

#<Symbol>
#<ElementValue Type="Preferred">CYP2A6</ElementValue>
#</Symbol>

for event, elem, in context:
    if event == "end" and elem.tag == "ClinVarSet":
        #print(elem)
        #print(dir(elem))
        #print(elem.find('Sample'))
        #print(elem.findall('Title'))
        #print(elem.items())
        #print(elem.getchildren())
        hpo_terms=list(set([x.text for x in elem.findall('.//TraitSet[@Type]/Trait[@Type]/Name/ElementValue[@Type="Preferred"]')]))
        #if not hpo_terms: continue
        #'<MeasureSet Type="Variant" ID="139581">'
        variant=[dict(x.items())['ID'] for x in elem.findall('.//MeasureSet[@Type="Variant"][@ID]')]
        #if not variant: continue
        #variant=dict(variant.items())
        locations=[dict(x.items()) for x in elem.findall('.//MeasureSet/Measure/SequenceLocation[@Assembly="GRCh37"]')]
        #chrom, start, end, ref, alt, = loc['Chr'], loc['start'], loc['end'], loc['referenceAllele'], loc['alternateAllele']
        accessions=[dict(x.items())['Acc'] for x in elem.findall('*/ClinVarAccession')]
        variant_ids=[]
        for loc in locations :
            variant_ids+=['-'.join([loc.get(h,'') for h in ['Chr','start','referenceAllele','alternateAllele']])]
        #print(variant['ID'])
        #print(hpo_terms)
        symbols=list(set([x.text for x in elem.findall('.//Symbol/ElementValue[@Type="Preferred"]')]))
        clinical_description=list(set([x.text for x in elem.findall('.//ClinicalSignificance/Description')]))[0]
        pubmed=list(set([x.text for x in elem.findall('.//ID[@Source="PubMed"]')]))
        #<XRef Type="rs" ID="1801272" DB="dbSNP"/>
        rs_numbers=[ 'rs'+dict(x.items())['ID'] for x in elem.findall('.//*[Type="rs"][@ID]')]
        #<Measure Type="copy number loss" ID="154792">
         #(elem.find('.//Measure[@Type="Variation"]') or elem.find('.//Measure[@Type="Deletion"]') or elem.find('.//Measure[@Type="Insertion"]'))
        if variant_ids and variant and hpo_terms:
            for v in variant_ids:
                if '---' not in v:
                    print(json.dumps({'variant_id':v,'accessions':accessions,'variant':variant[0],'phenotypes':hpo_terms,'clinical_description':clinical_description, 'symbols':symbols, 'pubmed':pubmed, 'rs_numbers':rs_numbers}))
        root.clear()
