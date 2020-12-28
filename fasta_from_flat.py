#!/usr/bin/python

import csv
import sys

 
filename = sys.argv[-1]
file=open(filename, mode='rU')

seqs=[]
names=[]
x=1

for line in file:
	seqs.append(line)
	names.append(x)
	x+=1

print len(seqs)
print len(names)

out_File=open('new_uniq.fa',mode='w')
for n in range(len(names)):
	out_File.write('>seq' + str(names[n]) + '\n' + seqs[n])
out_File.close()


