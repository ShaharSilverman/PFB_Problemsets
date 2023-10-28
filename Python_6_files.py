#!/usr/bin/env python

#Question_5:
#with open("Python_06.txt", "r") as Python_06_read, open("Python_06_uc.txt", "w") as Python_06_write:
#  for line in Python_06_read:
#    line = line.rstrip()
#    line = line.upper()
#    print(line)
#    Python_06_write.write(f"{line}")


#Question_7
#genes = {}
#with open ("Python_06.seq.txt", "r") as Python_06_seq_read:
#  for line in Python_06_seq_read:
#    line = line.rstrip()
#    line = line.upper()
#    reverse_dna1 = line.replace("A", "t").replace("T", "a").replace("C","g" ).replace("G", "c")
#    reverse_dna2 = reverse_dna1[::-1]
#    reverse_dna3 = reverse_dna2.upper()
#    gene_name, rev_comp_seq = reverse_dna3.split("\t")
#    genes[gene_name] = rev_comp_seq
#print(genes)


#Question_8:
#file_i = open('Python_06.fastq', 'r')
#count_line = 0
#count_character = 0

#for line in file_i:
#	line = line.rstrip()
#	count_line  += 1
#	count_character += len(line)
#average_line_length = count_character/count_line
#print(count_line)
#print(count_character)
#print(average_line_length)

#Question_9:
#import sys
#import re
#file_i = open(sys.argv[1], 'r')
#file_o = open('FASTA_file_out.fa', 'w')
#fastaDict = {}

#for line in file_i:
#	line = line.rstrip()
#	if re.match(r"^>",line):
#		header = line
#		fastaDict[header] = ''
#	else:
#		fastaDict[header] += line

#print(fastaDict)
#line = line.split()

#Question_10
import sys
alpaca_all = open('alpaca_all_genes.tsv', 'r')
alpaca_pig = open('alpaca_pigmentation_genes.tsv', 'r')
alpaca_stem = open('alpaca_stemcellproliferation_genes.tsv', 'r')
set_alpaca_all = set('')
set_alpaca_pig = set('')
set_alpaca_stem = set('')
for line in alpaca_all:
	line = line.rstrip()
	set_alpaca_all.add(line)
#print(set_alpaca_all)
for line in alpaca_pig:
	line = line.rstrip()
	set_alpaca_pig.add(line)
#print(set_alpaca_pig)
for line in alpaca_stem:
	line = line.rstrip()
	set_alpaca_stem.add(line)
print(set_alpaca_stem)

not_proliferation_genes = (set_alpaca_all - set_alpaca_stem)
also_not_proliferation_genes = (set_alpaca_pig - set_alpaca_stem)
stemcell_pro_pig = set_alpaca_pig | set_alpaca_stem

	




