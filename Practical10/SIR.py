#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#the total population
N=10000
#the infection probability upon contact
BETA=0.3
#the recovery probability
GAMMA=0.05
#initial infected/susceptible/recovered individuals 
infected=1
susceptible=N-infected
recovered=0
#susceptible/infected/recovered individuals
S=np.array([susceptible])
I=np.array([recovered])
R=np.array([infected])
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
	S=np.append(S,susceptible)
	I=np.append(I,infected)
	R=np.append(R,recovered)

#draw the graph for susceptible individuals
plt.plot(time,S,label="susceptible",color="blue",linewidth=2)
#draw the graph for infected individuals
plt.plot(time,I,label="infected",color="orange",linewidth=2)
#draw the graph for recovered individuals
plt.plot(time,R,label="recovered",color="green",linewidth=2)
#set the labels and the title
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
time_xticks=np.arange(0, len(time)+1, 200)
plt.xticks(time_xticks)
#show the graph
plt.legend()
plt.show()
plt.clf()
