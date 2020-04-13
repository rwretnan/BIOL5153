#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


re.search(pattern, string)
search(pattern, string)


# In[3]:


print(r"\t\n")


# In[4]:


dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
    print("restriction site found!")


# In[5]:


dna = "ATCGCGAATTCAC"
if re.search(r"GGACC", dna) or re.search(r"GGTCC", dna):
    print("restriction site found!")


# In[6]:


dna = "ATCGCGAATTCAC"
if re.search(r"GG(A|T)CC", dna):
    print("restriction site found!")


# In[7]:


dna = "ATCGCGAATTCAC"
if re.search(r"GC(A|T|G|C)GC", dna):
    print("restriction site found!")


# In[8]:


dna = "ATCGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna):
    print("restriction site found!")


# In[10]:


dna = "ATGACGTACGTACGACTG"

# store the match object in the variable m
m = re.search(r"GA[ATGC]{3}AC", dna)
print(m.group())


# In[11]:


dna = "ATGACGTACGTACGACTG"

# store the match object in the variable m
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("entire match: " + m.group())
print("first bit: " + m.group(1))
print("second bit: " + m.group(2))


# In[12]:


dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))


# In[13]:


dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))
print("group one start: " + str(m.start(1)))
print("group one end: " + str(m.end(1)))
print("group two start: " + str(m.start(2)))
print("group two end: " + str(m.end(2)))


# In[14]:


dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)


# In[15]:


dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r"[AT]{4,100}", dna)
print(runs)


# In[16]:


dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"[AT]{3,100}", dna)
for match in runs:
    run_start = match.start()
    run_end = match.end()
    print("AT rich region from " + str(run_start) + " to " + str(run_end))


# In[18]:


# Exercises

# Accession names

accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)


# In[20]:


for acc in accs:
    if re.search(r"(d|e)", acc):
        print("\t" + acc)


# In[21]:


for acc in accs:
    if re.search(r"d.*e", acc):
        print("\t" + acc)


# In[23]:


for acc in accs:
    if re.search(r"(d.e)", acc):
        print("\t" + acc)


# In[24]:


for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print("\t" + acc)


# In[25]:


for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)


# In[26]:


for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)


# In[27]:


for acc in accs:
    if re.search(r"[0123456789]{3,100}", acc):
        print("\t" + acc)


# In[28]:


for acc in accs:
    if re.search(r"\d{3,}", acc):
        print("\t" + acc)


# In[29]:


for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)


# In[33]:


# Double digest

import re
dna = open("dna.txt").read().rstrip("\n")
print("AbcI cuts at:")

for match in re.finditer(r"A[ATGC]TAAT", dna):
    print(match.start())


# In[34]:


import re
dna = open("dna.txt").read().rstrip("\n")
print("AbcI cuts at:")
for match in re.finditer(r"A[ATGC]TAAT", dna):
    print(match.start() + 3)


# In[32]:


import re
dna = open("dna.txt").read().rstrip("\n")
all_cuts = [0]
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)
all_cuts.append(len(dna))
print(all_cuts)


# In[35]:


for i in range(1,len(all_cuts)):
    this_cut_position = all_cuts[i]
    previous_cut_position = all_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("one fragment size is " + str(fragment_size))


# In[36]:


import re
dna = open("dna.txt").read().rstrip("\n")
all_cuts = [0]

# add cut positions for AbcI
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)

# add cut positions for AbcII
for match in re.finditer(r"GC[AG][AT]TG", dna):
    all_cuts.append(match.start() + 4)

# add the final position
all_cuts.append(len(dna))
print(all_cuts)


# In[37]:


import re
dna = open("dna.txt").read().rstrip("\n")
print(str(len(dna)))
all_cuts = [0]

# add cut positions for AbcI
for match in re.finditer(r"A[ATGC]TAAT", dna):
    all_cuts.append(match.start() + 3)

# add cut positions for AbcII
for match in re.finditer(r"GC[AG][AT]TG", dna):
    all_cuts.append(match.start() + 4)

# add the final position
all_cuts.append(len(dna))
sorted_cuts = sorted(all_cuts) 
print(sorted_cuts)

for i in range(1,len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position 
    print("one fragment size is " + str(fragment_size))


# In[ ]:




