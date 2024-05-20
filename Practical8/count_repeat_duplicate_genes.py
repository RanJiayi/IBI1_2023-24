#import the librery of regular expressions
import re

#open the file containing the sequences of genes which were created by whole genome duplication
import os
#Please change it to the correct path before you run the code
os.chdir("C:\\Users\\冉嘉忆\\OneDrive - International Campus, Zhejiang University\\桌面\\IBI\\new\\IBI1_2023-24\\文件")
duplication_sequence=open('duplicate_genes.fa')

#create	a file with the input filename
repetitive_sequence=input("please input one of the two repetitive sequences (‘GTGTGT’ or ‘GTCTGT’):")
if not (repetitive_sequence=='GTGTGT' or repetitive_sequence=='GTCTGT'):
	repetitive_sequence=input("please input one of the two repetitive sequences (‘GTGTGT’ or ‘GTCTGT’):")
else:
	new_file=open(f'{repetitive_sequence}_duplicate_genes.fa','w')

#put the gene name and the entire sequence on one line
transition_file=open('transition.fa','w')
for line in duplication_sequence:
	if line.startswith('>'):
		transition_file.write('\n'+line[:-1])
	else:
		transition_file.write(line[:-1])
transition_file=open('transition.fa')

for line in transition_file:
	#extract sequences containing the given repetitive element
	if re.search(str(repetitive_sequence),line):
		#count the number of instances
		repeat=re.findall(str(repetitive_sequence),line)
		number_instances=len(repeat)
		#extract the gene name
		gene_name=re.findall(r'>.+?\s',line)
		gene_name=''.join(str(i) for i in gene_name)
		#output the sequence name
		sequence_name=f'{gene_name} {number_instances}'
		new_file.write(sequence_name+'\n')
		#output the sequence
		sequence=re.sub(f'{gene_name}','',line)
		new_file.write(str(sequence))

#output the results
repetitive_element=open(f'{repetitive_sequence}_duplicate_genes.fa')
for line in repetitive_element:
	print(line)