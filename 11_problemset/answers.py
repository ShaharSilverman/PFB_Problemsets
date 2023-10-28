#!/usr/bin/env python3
class DNARecord(object):
	def __init__(self, sequence, gene_name, origin_organism):
		self.sequence = sequence
		self.gene_name = gene_name
		self.origin_organism = origin_organism
	def length(self):
		length = len(self.sequence)
		return length
	def nucleotide_comp(self):
		length = len(self.sequence)
		a_count = self.sequence.count('A')
		t_count = self.sequence.count('T')
		c_count = self.sequence.count('C')
		g_count = self.sequence.count('G')
		a_content = round((a_count/length)*100)
		t_content = round((t_count/length)*100)
		c_content = round((c_count/length)*100)
		g_content = round((g_count/length)*100)
		return (f"A: , {a_content}% ,T:  {t_content}% ,C: {c_content}% , G: {g_content}%")
	
	def GC_content(self):
		length = len(self.sequence)
		c_count = self.sequence.count('C')
		g_count = self.sequence.count('G')
		gc_content = ((c_count + g_count)/length)*100
		return (f"The GC content is: {gc_content}%")

	def FASTA_formatter(self):
		return(f">{self.gene_name}-{self.origin_organism} \n{self.sequence}")

dna_rec_obj_1 = DNARecord('ATGCTCTCAAATCAACA', 'P53', 'human')
dna_rec_obj_2 = DNARecord('ATGAAATTTCCCGGGCGCGCGAAA', 'OAS1', 'chimpanze')

for d in [dna_rec_obj_1, dna_rec_obj_2]:
	print('sequence: ', d.sequence, 'name: ', d.gene_name, 'organism of origin: ', d.origin_organism)
	print('length is: ' + str(d.length()))
	print('nucleotide content is: ' + str(d.nucleotide_comp()))
	print(str(d.GC_content()))
	print("FASTA format:\n "+ str(d.FASTA_formatter()))
