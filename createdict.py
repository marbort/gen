import json

ifile = open ("animali_dict_final","r")
lines=ifile.read().splitlines() 
a=[]
for i in range(1,len(lines)):
	a.append(i)

d=dict(zip(a,lines))



with open('animali.json', 'w') as fp:
    json.dump(d, fp)


