#create and print a dictionary to record the activities(key) and their time spent(value)
dic_day={'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'other':3.5}
print(dic_day)
#the requested activity that can be modified
activity_modified='Sleeping'
print(f'{activity_modified}:', dic_day[activity_modified])

#Import the graph module
import matplotlib.pyplot as plt
#indicate the used data
time_spent=list(dic_day.values())
#add label descriptions
activity=list(dic_day.keys())
plt.figure()
#construct a pie chart
plt.pie(time_spent,labels=activity,startangle=90)
plt.title('The average day of a university student')
plt.show()
plt.clf()
