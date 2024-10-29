import sys
import os.path
from os import path

import re

#output_name = "asm-rules.txt"
#output_file = open(filename_34, mode='w', encoding='utf-8')

args = len(sys.argv) - 1
#if (args == 0):
#do get the directory as input, assume current directory if no argument
for filename in os.listdir('.'):
	if filename.endswith('.adl'):
		print(filename)
		adl_file = open(filename,  encoding='utf-8')
		content = adl_file.read()
		##for line in adl_file:
		match = re.search(r'define\s+\(assembler.*};\s+// end of assembler block for asm_rules', content, re.DOTALL)
		if (match is not None):
			print(match.group(0))
		#pattern = re.compile(r"define\s+\(\s*assembler.*};\s+//\s+end of assembler block", re.VERBOSE | re.MULTILINE);
		#for match in pattern.finditer(content):
		#	print(match.group(0))
		adl_file.close()
#output_file.close()

#	if path.exists(filename) is False or path.isfile(filename) is False:
#		print("Error: invalid input (" + filename + "), expected filename of existing valid file") 
#		continue
#	filename_34 = filename + ".spt34"
#	file_28 = open(filename, encoding='utf-8')
#	file_34 = open(filename_34, mode='w', encoding='utf-8')
#	
#	if verbose:
#		print("[ " + filename + " -> " + filename_34 + " ]")
#	
#	lnum_28 = 0
#	lnum_34 = 0
#	for line_28 in file_28:
#		if verbose:
#			lnum_28 += 1
#			lnum_34 += 1
#			if re.search('^\s*maxs', line_28) is True and re.search('.no_maxsn', line_28) is False:
#				print("Note: (line " + str(lnum_28) + ") maxs -> (line " + str(lnum_34) + ") repeat + maxs, repeat instruction added as part of maxs translation")
#				lnum_34 += 1
#			elif re.search('^\s*rdx.+\.fft(8|16|32)', line_28):
#				print("Note: (line " + str(lnum_28) + ") rdx -> (line " + str(lnum_34) + ") repeat + rdx, repeat instruction added as part of rdx translation")
#				lnum_34 += 1
#		line_34 = translate(line_28)
#		file_34.write(line_34)
#
#	file_34.close()
#	file_28.close()
