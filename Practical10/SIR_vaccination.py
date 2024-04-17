#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


#the total population
N=10000
#the infection probability upon contact
BETA=0.3
#the recovery probability
GAMMA=0.05


for population in range(0,101,10):
	vaccinated=int(N*(population/100))
	if population==100:
		infected=0
	else:
		#initial infected/susceptible/recovered individuals 
		infected=1
		susceptible=N-vaccinated-infected
		recovered=0
	#infected individuals
	I=np.array([recovered])
	#loop count
	time=np.array([0])

	#repeat 1000 times
	for i in range(1,1001): 
		time=np.append(time,i)
		#recovery status each time
		status_recovery=np.random.choice(range(2),infected,p=[1-GAMMA,GAMMA])
		#sum over all recovered individuals
		recovered_change=0
		for m in status_recovery:
			recovered_change+=m
		recovered=recovered+recovered_change
		infected=infected-recovered_change
		#probability of infection
		P=BETA*(infected/N)
		#infection status each time
		status_infection=np.random.choice(range(2),susceptible,p=[1-P,P])
		#sum over all infected individuals
		infected_change=0
		for n in status_infection:
			infected_change+=n
		infected=infected+infected_change
		susceptible=susceptible-infected_change
		I=np.append(I,infected)	

	#draw the graph for infected individuals
	plt.plot(time,I,label="{:.0f}%".format(population),color=cm.terrain(population),linewidth=2)


#set the labels and the title
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
time_xticks=np.arange(0, len(time)+1, 200)
plt.xticks(time_xticks)
#show the graph
plt.legend()
plt.show()
plt.clf()
