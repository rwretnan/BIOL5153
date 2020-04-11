#! /bin/bash

# open the file
my_file = open("dna.txt")

# read the contents
my_dna = my_file.read()

# calculate the length
length = len(my_dna)

# count the percentage of A, T, C, and G
A_count = my_dna.count("A")
T_count = my_dna.count("T")
C_count = my_dna.count("C")
G_count = my_dna.count("G")

percentage_A = (A_count / length) * 100
percentage_T = (T_count / length) * 100
percentage_C = (C_count / length) * 100
percentage_G = (G_count / length) * 100


# print the output
print("the DNA length is " + length)
print("percent A " + '{:.5}'.format(str(percentage_A)) + "%")
print("percent T " + '{:.5}'.format(str(percentage_T)) + "%")
print("percenr C " + '{:.5}'.format(str(percentage_C)) + "%")
print("percent G " + '{:.5}'.format(str(percentage_G)) + "%")

my_file.close()