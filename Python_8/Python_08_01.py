#!/usr/bin/env python3
import re

#open the FASTA file as file_i for reading
file_i = open('Python_08.fasta', 'r')
#define seq_dict as a dictionart
seq_dict = {}
#assign an empty string to gene_name
gene_name = ''
#open a for loop that reads every line in file_i and removes new line
for line in file_i:
	line = line.rstrip()
#if there's > at the begining of the line, add the line to the string	
	if re.match(r"^>", line):
		gene_name = line
#the gene name is a key for another dictionary in which the keys are: A, T, G, and C, currently their value is 0. 
		seq_dict[gene_name] = {
		'A':0, 'T':0, 'G':0, 'C':0}
#if the line doesn't start with > it means that it starts with a nucleotide and every key will be paired with the count of it's respective nucleotide. 
	else:
		for nucleotide in line:
			seq_dict[gene_name][nucleotide] +=1
			print(seq_dict)

