#!/usr/bin/env python3

import re
file_i = open('Python_07_ApoI.fasta', 'r')
for line in file_i:
	line = line.rstrip()
	for restriction_site in re.findall(r"([GA]AATT[TC])", line):
		print(restriction_site)
	
#		new_line = re.sub(r'[GA]AATT[TC]', '[GA]\^AATT[TC]', line)
#		print(new_line)
