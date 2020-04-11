#! /bin/bash

#assn01-1

$find /home -name ‘nad*’

#assn01-2 

$top 

#Processes: 478 total, 2 running, 476 sleeping, 1594 threads                                                                                     13:24:19
Load Avg: 1.52, 1.21, 1.18  CPU usage: 0.35% user, 0.71% sys, 98.93% idle  SharedLibs: 243M resident, 44M data, 14M linkedit.
MemRegions: 91784 total, 2079M resident, 143M private, 1609M shared. PhysMem: 8005M used (2068M wired), 185M unused.
VM: 2568G vsize, 1880M framework vsize, 35285140(0) swapins, 36475201(0) swapouts. Networks: packets: 10009304/7828M in, 21977064/21G out.
Disks: 6924991/305G read, 2669311/214G written.

#assn01-3

$grep misc_feature watermelon.gff | sort -k7gr watermelon.gff > IR_region.gff

#assn01-4

$grep -c IR IR_region.gff; grep —v -c IR IR_region.gff 

#IR: 4; non IR: 140

#assn01-5 

$cd watermelon_nt; $grep -vB1 GAATTC *.fasta | grep -B1 GGATCC *.fasta

#assn01-6

$cd; $cd Desktop/example_files; $ls; $head -n1000 shaver_etal.csv | tail -n501 shaver_etal.csv 


#assn01-7

$cd /Users/ririretnaningtyas/Desktop/example_files; $column fruit.txt | sort -k2r,2 -k3,3 fruit.txt  
