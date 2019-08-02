ifile=open("santi","r")
omaschile=open("maschile.txt","a")
ofemminile=open("femminile.txt","a")

lines=ifile.readlines()
lines_strip=[]
for i in range (1,len(lines)):
   lines_strip.append(lines[i].strip())
femminile=[]
maschile=[]
#print(lines_strip)

for item in lines_strip:
# print(item[-1:])
   if "a" in item[-1:]:
       femminile.append(item+"\n") 
   else:
        maschile.append(item+"\n")

for i in range (1,len(maschile)):
    omaschile.write(maschile[i])
for i in range(1,len(femminile)):
    ofemminile.write(femminile[i])

      



