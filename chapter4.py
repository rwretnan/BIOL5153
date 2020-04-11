#!/usr/bin/env python
# coding: utf-8

# In[1]:


# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"


# In[15]:


# set the values of all the header variables 
header_1 = "ABC123"
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


# In[7]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
print(apes[0])
first_site = conserved_sites[2]


# In[8]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1


# In[9]:


last_apes = apes[-1]


# In[10]:


ranks = ["kingdom", "phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# lower ranks are class, order and family


# In[11]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
apes.append("Pan paniscus")


# In[12]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print("There are " + str(len(apes)) + " apes")
apes.append("Pan paniscus")
print("Now there are " + str(len(apes)) + " apes")


# In[16]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys

print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")


# In[17]:


ranks = ["kingdom", "phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
ranks.reverse()
print("after reversing : " + str(ranks))
ranks.sort()
print("after sorting : " + str(ranks))


# In[18]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]


# In[19]:


print(apes[0] + " is an ape")
print(apes[1] + " is an ape")
print(apes[2] + " is an ape")


# In[21]:


for ape in apes:
    print(ape + " is an ape")


# In[22]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes: 
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")


# In[26]:


apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes:
    name_length = len(ape)
first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")


# In[27]:


name = "Martin"
for character in name:
    print("one character is " + character)


# In[28]:


names = "melanogaster, simulans, yakuba, ananassae"
species = names.split(",")
print(str(species))


# In[29]:


file = open("some_input.txt")
for line in file: 
    # do something with the line


# In[30]:


protein = "vlspadktnv"
stop_positions = [3,4,5,6,7,8,9,10]
for stop in stop_positions:
    substring = protein[0:stop]
    print(substring)


# In[32]:


for number in range(6):
    print(number)


# In[33]:


for number in range(3, 8):
    print(number)


# In[34]:


for number in range(2, 14, 4):
    print(number)


# In[36]:


# Exercises

#Processing DNA in a file

file = open("input.txt")
for dna in file: 
    print(dna)


# In[37]:


file = open("input.txt")
for dna in file: 
    last_character_position = len(dna)
    trimmed_dna = dna[14:last_character_position]
    print(trimmed_dna)


# In[39]:


file = open("input.txt")
output = open("trimmed.txt", "w")
for dna in file:
    last_character_position = len(dna)
    trimmed_dna = dna[14:last_character_position]
    output.write(trimmed_dna)


# In[40]:


# open the input file
file = open("input.txt")

#open the output file
output = open("trimmed.txt", "w")

# go through the input file one line at a time
for dna in file:
    
    # calculate the position of the last character
    last_character_position = len(dna)
    
    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:last_character_position]
    
    # print out the trimmed sequence
    output.write(trimmed_dna)
    
    # print out the length to the screen
    print("processed sequence with length " + str(len(trimmed_dna)))


# In[ ]:




