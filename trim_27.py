#!/usr/bin/python
import sys
filename = sys.argv[-1]
seqs=open(filename, mode='rU')
a=0
trim_seqs=[]
names=[]


for line in seqs:
        L=line.strip()
        if L[0] == '>':
                names.append(L)
        else:
                a=L[0:27]
                trim_seqs.append(a)
                
print(len(names))
print(len(trim_seqs))

out_File=open('trim27_output.txt',mode='w')
for n in range(len(names)):
        out_File.write(names[n] + '\n' + trim_seqs[n] + '\n')
