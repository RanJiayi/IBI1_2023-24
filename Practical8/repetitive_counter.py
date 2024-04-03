#import the librery of regular expressions
import re
#create	a string variable seq
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#extract the strings of repeat elements
repeat_1=re.findall(r'GTGTGT',seq)
repeat_2=re.findall(r'GTCTGT',seq)
#count the total number of repeat elements
total=len(repeat_1)+len(repeat_2)
print(total)
