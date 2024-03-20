#create a dictionary to record the activities(key) and their time spent(value)
dic_day={'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'other':3.5}
#the requested activity that can be modified
activity_modified='Sleeping'
print(dic_day[activity_modified])

#Import the graph module
import matplotlib.pyplot as plt
#indicate the used data
time_spent=[8,6,3.5,2,1,3.5]
#add label descriptions
activity=['Sleeping','Classes','Studying','TV','Music','other']
plt.figure()
#construct a pie chart
plt.pie(time_spent,labels=activity,startangle=90)
plt.show()
plt.clf()
