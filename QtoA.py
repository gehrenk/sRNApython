#!/usr/bin/python
from Bio import SeqIO
import sys
filename= sys.argv[-1]
count = SeqIO.convert(filename, "fastq", "new.fa", "fasta")
print(count)

