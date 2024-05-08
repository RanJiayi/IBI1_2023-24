import re
import blosum as bl
matrix = bl.BLOSUM(62)

#calculate the Hamming distance
def distance(seq_1,seq_2):
	distance=0
	#Compare the two amino acid sequences
	for i in range(len(seq_1)):
		if seq_1[i]!=seq_2[i]:
			#count the number of amino acids that are not identical in two pairwise sequences
			distance+=1
	return distance
#calculate the alignment score
def score(seq_1,seq_2):
	score=0
	#Compare the two amino acid sequences
	for i in range(len(seq_1)):
		#find score
		val=matrix[seq_1[i]][seq_2[i]]
		#sum scores
		score+=val
	return score


#read the file
import os
os.chdir("C:\\Users\\冉嘉忆\\OneDrive - International Campus, Zhejiang University\\桌面\\IBI\\new\\IBI1_2023-24\\文件")
file_1=open('SLC6A4_HUMAN.fa','r')
file_2=open('SLC6A4_MOUSE.fa','r')
file_3=open('SLC6A4_RAT.fa','r')
#extract the sequence
seq_1=''
seq_2=''
seq_3=''
for line in file_1:
	if line[0]!='>':
		seq_1+=line.strip()
for line in file_2:
	if line[0]!='>':
		seq_2+=line.strip()
for line in file_3:
	if line[0]!='>':
		seq_3+=line.strip()

#use the functions to generate the Hamming distance and alignment score for each of the three comparisons
distance_1=distance(seq_1,seq_2)
distance_2=distance(seq_1,seq_3)
distance_3=distance(seq_2,seq_3)
score_1=score(seq_1,seq_2)
score_2=score(seq_1,seq_3)
score_3=score(seq_2,seq_3)
#calculate the percentage of identical amino acids for each of the three comparisons
per_1=1-distance_1/len(seq_1)
per_2=1-distance_2/len(seq_1)
per_3=1-distance_3/len(seq_1)
print(f'HUMAN-MOUSE: the alighment score is {score_1}, the percentage of identical amino acids is {per_1}.')
print(f'HUMAN-RAT: the alighment score is {score_2}, the percentage of identical amino acids is {per_2}.')
print(f'MOUSE-RAT: the alighment score is {score_3}, the percentage of identical amino acids is {per_3}.')

