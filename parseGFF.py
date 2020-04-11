#! /usr/bin/env python3

#define the input file 
watermelonfile = []

#open the file and read it

with open("/Users/ririretnaningtyas/Desktop/watermelon_files/watermelon.gff", "rt") as my_file:
	for line in my_file:
	gene = line.split() [10] 
	
	if not gene == "similar":   #ignore the similar to
	watermelonfile.append(gene)
	
# sort the list
	watermelonfile.sort()
	print(watermelonfile)
