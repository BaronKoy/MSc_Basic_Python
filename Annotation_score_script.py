#Script for patient annotation score
#Edited: 20/05/2017

#packages
import requests
import pymongo
import json
import sys

#database
client = pymongo.MongoClient(host='*************', port=*****)
patients_db = client['patients']

#NP example
for patient in patients_db.patients.find():
    p=patient
    x=dict()
    x['id']=p['report_id']
    x['features']=p['features']
    for f in p['features']:
        f['isPresent']={'yes':'true','no':'false'}[f['observed']]
        del f['observed']
        del f['label']
        del f['type']
	y=json.dumps(x)
	url='https://monarchinitiative.org/score/?annotation_profile={}'.format(y)
    r=requests.get(url,headers={'Content-Type':'application/json'})
    d=r.json()
    print p['external_id'],d['simple_score']
