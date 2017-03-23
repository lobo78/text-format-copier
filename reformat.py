#!/usr/bin/python
# Licensed under the MIT License, 
# https://opensource.org/licenses/MIT

# Having two files with the same text but different newlines, format one file to match the other.
# https://github.com/lobo78/text-format-copier.git

import sys
import re

def extract_patterns(filename):
	f = open(filename, 'rU')
	text = f.read()
	
	# Match four words, then 2 newlines, then four words
	newline_matches = re.findall(r"((?:\S* \S*){3})(?:\n\n|$)((?:\S* \S*){3})", text)
	return newline_matches

def reformat(filename, patterns):
	reformatted = ""
	f = open(filename, 'rU')
	text = f.read()
	text = re.sub(r"\n", r" ", text)
	
	for p_tuple in patterns:
		(end_string, start_string) = p_tuple
		text = re.sub(end_string + r" " + start_string, end_string + r"\n\n" + start_string, text, 1)
	
	f = open(filename + ".formatted", "w")
	f.write(text)
	
def main():
	args = sys.argv[1:]
	
	if not args:
		print 'usage: sourcefile unformattedfile'
		sys.exit(0)
		
	sourcefile = args[0]
	unformattedfile = args[1]
	
	patterns = extract_patterns(sourcefile)
	reformat(unformattedfile, patterns)
	
if __name__ == '__main__':
	main()