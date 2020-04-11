#! /bin/bash

#assn03-1

#! /bin/bash
for R in (seq 808 8008)
do 
echo TR-$R 
done

#assn03-2

alias "r"= grep
alias "l"= ls 


#assn03-3

echo *.fasta | wc -l 

#assn03-4
echo *.tre | wc -l

#assn03-5
echo *sched | wc -l

#assn03-6 

#! bin/bash
for trees in *.fasta 
do
if [[ -e ${trees%.fasta}_raxml.tre ]] 
then 
continue 
else 
echo 'no tree'
fi 
done

#assn03-7
grep 'Program Return Code: 0' *.sched | uniq | wc -l
grep 'Program Return Code: *' *.sched | uniq | grep -v '0' | wc -l


#assn03-8

#!/bin/bash 
for ii in *.fasta 
do
if [[ -e ${trees%.fasta}_raxml.tre ]] 
then 
continue 
else 
write_raxml_job_script.py OG0023009_alignment.fasta > OG0023009_alignment.pbs
fi 
done