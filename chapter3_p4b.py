#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_file = open ("dna.txt")


# In[3]:


print(my_file)


# In[4]:


my_string = 'abcdefg'
print(my_string)
my_number = 42
print(my_number + 1)


# In[5]:


my_file = open ("dna.txt")
file_contents = my_file.read()
print(file_contents)


# In[6]:


my_file_name = "dna.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()


# In[7]:


apple = "dna.txt"
banana = open(apple)
grape = banana.read()


# In[8]:


my_file_name = "dna.txt"
my_contents = my_file_name.read()


# In[1]:


my_file_name = "dna.txt"
my_file = open(my_file_name)
print(my_file)


# In[2]:


# open the file
my_file = open("dna.txt")
# read the contents
my_dna = my_file.read()
# calculate the length
dna_length = len(my_dna)
# print the output
print("sequence is " + my_dna + " and length is " + str(dna_length))


# In[4]:


my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove the new line from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_lenght = len(my_dna)
print("sequence is " + my_dna + " and length is " + str(dna_length))


# In[8]:


my_file_contents = my_file.read()
my_dna = my_file_contents.rstrip("\n")


# In[9]:


my_dna = my_file.read().rstrip("\n")


# In[10]:


my_file = open("nonexistent.txt")


# In[11]:


my_file = open("out.txt", "w")
my_file.write("Hello world")


# In[14]:


# write "abcdef"
my_file.write("abc" + "def")
# write "8"
my_file.write(str(len('AGTGCTAG')))
# write "TTGC"
my_file.write("ATGC".replace('A', 'T'))
# write "atgc"
my_file.write("ATGC".lower())
# write contents of my_variable 
my_file.write("my_variable")


# In[15]:


my_file = open("out.txt", "w")
my_file.write("Hello world")
# remember to close the file
my_file.close()


# In[16]:


my_file = open("/Users/ririretnaningtyas/Desktop/Biol5153/python/myfile.txt")


# In[17]:


my_file.close()


# In[21]:


# Exercise 
# Splitting genomic DNA
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(exon1 + intron.lower() + exon2)


# In[22]:


# Splitting genomic DNA
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()


# In[23]:


coding_file = open("coding_dna.txt", "w") 
noncoding_file = open("noncoding_dna.txt", "w")


# In[25]:


coding_file.write(exon1 + exon2) 
noncoding_file.write(intron)


# In[26]:


# open the file and read its content
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()

# extract the different bits of DNA sequence
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]

# open the two output files
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")

# write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)


# In[27]:


# Writing a FASTA file

header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"


# In[28]:


# writing a FASTA file

print(header_1)
print(seq_1)
print(header_2)
print(seq_2)
print(header_3)
print(seq_3)


# In[29]:


print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2)
print('>' + header_3 + '\n' + seq_3)


# In[30]:


print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2.upper())
print('>' + header_3 + '\n' + seq_3.replace('-', ''))


# In[31]:


output = open("sequences.fasta", "w")
output.write('>' + header_1 + '\n' + seq_1) 
output.write('>' + header_2 + '\n' + seq_2.upper()) 
output.write('>' + header_3 + '\n' + seq_3.replace('-', ''))


# In[32]:


output = open("sequences.fasta", "w")
output.write('>' + header_1 + '\n' + seq_1 + '\n')
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')


# In[33]:


# set the values of all the header variables header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# make a new file to hold the output
output = open("sequences.fasta", "w")

# write the header and sequence for seq1 
output.write('>' + header_1 + '\n' + seq_1 + '\n')

# write the header and uppercase sequences for seq2
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')

# write the header and sequence for seq3 with hyphens removed
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')


# In[34]:


# Exercise
# Writing multiple FASTA files

output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")


# In[35]:


# set the values of all the header variables header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables 
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# make three files to hold the output 
output_1 = open(header_1 + ".fasta", "w") 
output_2 = open(header_2 + ".fasta", "w") 
output_3 = open(header_3 + ".fasta", "w")

# write one sequence to each output file
output_1.write('>' + header_1 + '\n' + seq_1 + '\n') 
output_2.write('>' + header_2 + '\n' + seq_2.upper() + '\n') 
output_3.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')


# In[ ]:




