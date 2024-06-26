#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


#create a model of the given geographical area
population=np.zeros((100,100))
#choose a random point for where the outbreak happens
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.imshow(population,cmap='viridis',interpolation='nearest')
plt.show()
plt.clf()
#the infection probability upon contact
BETA=0.3
#the recovery probability
GAMMA=0.05

#repeat for 100 times
for j in range(1,101):
	infectedIndex = np.where(population==1)
	# find all infected points
	for i in range(len(infectedIndex[0])):
	    x = infectedIndex[0][i]
	    y = infectedIndex[1][i]
	    #address all the neighbours
	    for xNeighbour in range(x-1,x+2):
	        for yNeighbour in range(y-1,y+2):
	            #exclude the initial point
	            if (xNeighbour,yNeighbour) != (x,y):
	                #exclude the edge
	                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
	                    #find the susceptible neighbours
	                    if population[xNeighbour,yNeighbour]==0:
	                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-BETA,BETA])[0]
	#recovered individuals
	for m in range(population.shape[0]):
		for n in range(population.shape[1]):
			if population[m,n]==1:
				population[m,n]=np.random.choice(range(1,3),1,p=[1-GAMMA,GAMMA])[0]

	#draw the heat map
	if j%10==0:
		plt.imshow(population,cmap='viridis',interpolation='nearest')
		plt.show()
		plt.clf()