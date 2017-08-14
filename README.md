# MSc Genetics of Human Disease
Code to split and read files

These files were used to navigate through various methods and the tools used for my MSc project on sorting and scoring of
patient phenotypes within the Phenopolis database.
The scripts are also my first attempt at using the python language in a practical setting.

```#alternative print function
from __future__ import print_function
#packages
import pymongo
import re

#machine holding patient information
conn = pymongo.MongoClient(host='************.ac.uk', port=*****)

#dictionary that holds all variant and patient information
variants_db=conn['uclex']
patients_db=conn['patients']

#listing patients with genes
patient=patients_db.patients.find_one({'external_id':'Prionb2_Sample_8000'})
print (patient)
```
