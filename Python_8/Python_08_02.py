#!/usr/bin/env python3
import re
#open the FASTA file as file_i for reading
file_i = open('Python_08.fasta', 'r')
seq_dict = {}
gene_name = ''
#open a for loop that reads every line in file_i and removes new li    ne
for line in file_i:
	line = line.rstrip()
	if re.match(r"^>", line):
		gene_name = line
		if re.match(r"ATG[ATGC]*[[TAA][TAG][TGA]"
		seq_dict[gene_name] = {
