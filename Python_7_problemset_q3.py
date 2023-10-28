#!/usr/bin/env python

import re
file_i = open('Python_07.fasta', 'r')
file_o = open('Python_out_fasta', 'w')
headers = ''

new_string = ''
for line in file_i:
  line = line.rstrip()
  if re.match(r'^>',line):
    headers = headers + line  

#print(headers)

found = re.findall(r">(\S+)\s+(.*)(>\S+)\s+(.*)", headers)

print("id:", found[0][0], "\ndescription:", found[0][1], "\nid:", found[0][2], "\ndescription:", found[0][3])




