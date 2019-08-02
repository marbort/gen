import json

ifile = open ("santi_ordered.txt","r")
lines=ifile.read().splitlines() 
a=[]
for i in range(1,len(lines)):
	a.append(i)

d=dict(zip(a,lines))



with open('santi.json', 'w') as fp:
    json.dump(d, fp)


