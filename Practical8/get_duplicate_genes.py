#import the librery of regular expressions
import re

#read the file
import os
os.chdir("C:\\Users\\冉嘉忆\\OneDrive - International Campus, Zhejiang University\\桌面\\IBI\\new\\IBI1_2023-24\\文件")
initial=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#store the simplified sequence in a new file
simplified_file=open('duplicate_genes.fa','w')

#indicate whether the sequence description contains the word ‘duplication’
duplication=False

for line in initial:
	#look through the sequence description
	if line.startswith('>'):
		#extract sequence description containing the word ‘duplication’
		if re.search('duplication',line):
			duplication=True
			gene_name=re.findall(r'>.+?_mRNA',line)
			gene_name=''.join(str(i) for i in gene_name)
			simplified_file.write(gene_name+'\n')
		#skip the sequence description without the word ‘duplication’
		else:
			duplication=False
	#look through the gene sequence
	else:
		#write the sequences corresponding to the extracted description
		if duplication==True:
			simplified_file.write(line)

#output the results
simplified=open('duplicate_genes.fa')
for line in simplified:
	print(line)
