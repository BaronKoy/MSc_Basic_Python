from os.path import basename
f= open("input_file.txt")
x=[]
for l in f.readlines():
	x.append(l.strip())

#blah
d=dict()
for a in x:
	y=basename(a).split('_')
	sample=y[0]
	if sample not in d:
		d[sample]=[a]
	else:
		d[sample].append(a)

print d


import pymongo
conn = pymongo.MongoClient(host='phenotips.cs.ucl.ac.uk', port=27017)
db=conn['patients']
db.patients.find()
db.patients.find_one()
[x for x in db.patients.find({'sex':'F'})]

	
