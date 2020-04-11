#!/usr/bin/env python
# coding: utf-8

# In[1]:


# hello world 
print("Hello world")


# In[2]:


# Hello world
print("Hello world")
print('Hello world')


# In[3]:


# She said Hello
print("She said, 'Hello world'")
print('She said, "Hello world"')


# In[4]:


# this is a comment, it will be ignored by the computer
print("Comments are very useful!")


# In[5]:


# print a friendly greeting
print("Hello world")


# In[6]:


print(hello world)


# In[7]:


prin("Hello world")


# In[8]:


print("Hello
      world")


# In[9]:


# how to include a new line in the middle of a string 
print("Hello\nworld")


# In[13]:


# store a short DNA sequence in the variable my_dna
my_dna = "ATGCGTA"
#now print the DNA sequence
print(my_dna)
# change the value of my_dna 
my_dna = "TGGTCCA"
# store a short DNA sequence in the variable banana
banana = "ATGCGTA"
print(banana)
print(my_dna)


# In[14]:


my_file = "my_file.txt"


# In[15]:


my_dna = "AATT" + "GGCC"
print(my_dna)


# In[16]:


upstream = "AAA"
my_dna = upstream + "ATGC"
# my_dna is now "AAAATGC"
print(my_dna)


# In[17]:


upstream = "AAA"
downstream = "GGG"
my_dna = upstream + "ATGC" + downstream
# my_dna is now "AAAATGCGGG"
print(my_dna)


# In[19]:


print("Hello" + "" + "world")
print("Hello" + " " + "world")


# In[20]:


# this line doesn't produce any output
len("ATGC")


# In[21]:


dna_length = len("AGTC")
print(dna_length)


# In[22]:


# store the DNA sequence in a variable 
my_dna = "ATGCGAGT"
# calculate the length of the sequence and store it in a variable 
dna_length = len(my_dna)
#print a message telling us the DNA sequence length
print("The length of the DNA sequence is" + dna_length)


# In[26]:


my_dna = "ATGCGAGT"
dna_length = len(my_dna)
print("The length of the DNA sequence is" + " " + str(dna_length))


# In[27]:


my_dna = "ATGC"
#print my_dna in lower case
print(my_dna.lower())


# In[28]:


print("ATGC")
len(my_dna)


# In[29]:


my_dna = "ATGC"
# print the variable
print("before: " + my_dna)
#run the lower method and store the result
lowercase_dna = my_dna.lower()
# print the variable again
print("after: " + my_dna)


# In[1]:


my_number = len("ATGC")
# my number is 4
print(my_number.lower())


# In[3]:


protein = "vlspadktnv"
#replace valine with tyrosine
print(protein.replace("v", "y"))
# we can replace more than one character
print(protein.replace("vls", "ymt"))
#the original variable is not affected
print(protein)


# In[4]:


protein = "vlspadktnv"
# print positions three to five
print(protein[3:5])
# position starts at zero, not one
print(protein[0:6])
# if we use a stop position beyon the end, it's the same as using the end 
print(protein[0:60])


# In[6]:


protein = "vlspadktnv"
first_residue = protein[0]
print(first_residue)


# In[8]:


protein = "vlspadktnv"
# count amino acid residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')

# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))


# In[9]:


protein = "vlspadktnv"
print(str(protein.find('p')))
print(str(protein.find('kt')))
print(str(protein.find('w')))


# In[12]:


# Exercise

# Calculating AT content
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

print("length: " + str(length))
print("A count: " + str(a_count))
print("T count: " + str(t_count))


# In[13]:


test_dna = "ATGC"
length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')

print("length: " + str(length))
print("A count: " + str(a_count))
print("T count: " + str(t_count))


# In[14]:


test_dna = "ATGC"
length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')


at_content = a_count + t_count / length
print("AT content is " + str(at_content))


# In[18]:


at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))


# In[19]:


# Calculating AT content
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))


# In[20]:


# Complementing DNA
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# replace A with T
replacement1 = my_dna.replace('A', 'T')
# replace T with A
replacement2 = replacement1.replace('T', 'A')
# replace C with G
replacement3 = replacement2.replace('C', 'G')
# replace G with C
replacement4 = replacement3.replace('G', 'C')
# print the result of the final replacement
print(replacement4)


# In[21]:


# Complementing DNA
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# replace A with T
replacement1 = my_dna.replace('A', 'T')
print(replacement1)
# replace T with A
replacement2 = replacement1.replace('T', 'A')
print(replacement2)
# replace C with G
replacement3 = replacement2.replace('C', 'G')
print(replacement3)
# replace G with C
replacement4 = replacement3.replace('G', 'C')
print(replacement4)


# In[22]:


my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 'H')
replacement2 = replacement1.replace('T', 'J')
replacement3 = replacement2.replace('C', 'K')
replacement4 = replacement3.replace('G', 'L')
replacement5 = replacement4.replace('H', 'T')
replacement6 = replacement5.replace('J', 'A')
replacement7 = replacement6.replace('K', 'G')
replacement8 = replacement7.replace('L', 'C')
print(replacement8)


# In[23]:


# Complementing DNA

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# replace A with T
replacement1 = my_dna.replace('A', 't')
print(replacement1)
# replace T with A
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
# replace C with G
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
# replace G with C
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())


# In[25]:


# Restriction fragment lengths

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))


# In[26]:


# Splicing out introns, part one 
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:63]
exon2 = my_dna[91:10000]
print(exon1 + exon2)


# In[28]:


# Splicing out introns
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)


# In[29]:


# Splicing out introns, part two
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(coding_length / total_length)


# In[30]:


# Splicing out introns, part two
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
exon2 = my_dna[90:10000]
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(100 * coding_length / total_length)


# In[31]:


# Splicing out introns, part three
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(exon1 + intron.lower() + exon2)


# In[32]:


# Splicing out introns, part three
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
intron = my_dna[62:90].lower()
exon2 = my_dna[90:10000]
print(exon1 + intron + exon2)


# In[33]:


# Splicing out introns, part three
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[1:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(my_dna[1:62] + my_dna[62:90].lower() + my_dna[90:10000])


# In[ ]:




