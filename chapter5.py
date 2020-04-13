#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length 
print("AT content is" + str(at_content))


# In[3]:


def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content


# In[4]:


get_at_content("ATGACTGGACCA")


# In[5]:


at_content = get_at_content("ATGACTGGACCA")
print("AT content is " + str(get_at_content("ATGACTGGACCA")))


# In[6]:


def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_content + t_count) / length
    return at_content

print(a_count)


# In[7]:


def get_at_content(dna): 
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))


# In[8]:


def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))


# In[10]:


def get_at_content(dna, sig_figs):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))


# In[11]:


def get_a_number():
    return 42


# In[12]:


def get_at_content():
    dna = "ACTGATGCTAGCTA"
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)


# In[13]:


def get_at_content():
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)

dna = "ACTGATCGATCG"
print(get_at_content())


# In[14]:


def print_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    print(str(round(at_content, 2)))


# In[23]:


get_at_content("ACTGATCGATCG", 2)
get_at_content(dna= "ATCGTGACTCG", sig_figs=2)
get_at_content(sig_figs=2, dna="ATCGTGACTCG")
get_at_content("ATCGTGACTCG", sig_figs=2)
get_at_content(dna="ATCGTGACTCG", 2)


# In[24]:


def get_at_content(dna, sig_figs=2):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)


# In[25]:


get_at_content("ATCGTGACTCG") 
get_at_content("ATCGTGACTCG", 3)
get_at_content("ATCGTGACTCG", sig_figs=4)


# In[26]:


assert get_at_content("ATGC") == 0.5


# In[27]:


assert get_at_content("ATGCNNNNNNNNNN") == 0.5


# In[28]:


def get_at_content(dna, sig_figs=2):
    dna = dna.replace('N', '')
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length 
    return round(at_content, sig_figs)


# In[30]:


assert get_at_content("A") == 1
assert get_at_content("G") == 0
assert get_at_content("ATGC") == 0.5 
assert get_at_content("AGG") == 0.33 
assert get_at_content("AGG", 1) == 0.3 
assert get_at_content("AGG", 5) == 0.33333


# In[35]:


# Exercises

#Percentage of amino acid residues, part one

protein = "MSRSLLLRFLLFLLLLPPLP"
aa = "R"
aa_count = protein.count(aa)
protein_length = len(protein)
percentage = aa_count * 100 / protein_length 
print(percentage)

def get_aa_percentage(protein, aa):
    aa_count = protein.count(aa)
    protein_length = len(protein)
    percentage = aa_count * 100 / protein_length
    return percentage

# test the function with assertions
assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


# In[38]:


def get_aa_percentage(protein, aa):
    # convert both inputs to upper case 
    protein = protein.upper()
    aa = aa.upper()
    
    aa_count = protein.count(aa)
    protein_length = len(protein)
    percentage = aa_count * 100 / protein_length
    return percentage


# In[40]:


# Exercises

# Percentage of amino acid residues, part two

protein = "MSRSLLLRFLLFLLLLPPLP"
aa_list = ['M', 'L', 'F']

# the total variable will hold the total number of matching residues 
total = 0
for aa in aa_list:
    print("counting number of " + aa) 
    aa = aa.upper()
    aa_count = protein.count(aa)
    
# add the number for this residue to the total count
total = total + aa_count
print("running total is " + str(total))

percentage = total * 100 / len(protein)
print("final percentage is " + str(percentage))


# In[44]:


def get_aa_percentage(protein, aa_list):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
percentage = total * 100 / protein_length
return percentage


# In[47]:


def get_aa_percentage(protein, aa_list=['A','I','L','M','F','W','Y','V']):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
percentage = total * 100 / protein_length
return percentage


# In[ ]:




