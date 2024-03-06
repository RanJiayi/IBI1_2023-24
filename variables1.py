a=40
b=36
c=30
d=a-b
e=b-c
m=(d>e)
#e is greater than d, so a combination of running and strength training had a greater improvemrnt on running time
if m==False:
    print("e is greater than d. A combination of running and strength training had a greater improvemrnt on running time.")
elif m==True:
    print("d is greater than e. Running and strength training had a greater improvemrnt on running time.")
else:
    print("d and e are equal. The two training regimes had the same effects on running time.")
