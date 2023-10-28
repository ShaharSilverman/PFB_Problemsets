#!/usr/bin/env python3
import re 
import sys

file_i = sys.argv[1]
width = int(sys.argv[2])
dna = open(file_i, 'r')

for line in dna: 
	line = line.rstrip()
	dna = line
def split_nt_string(dna,width):
	new_string = re.findall("\w{1,80}", dna)
	for x in new_string:
		print(x)



split_nt_string(dna, width)






