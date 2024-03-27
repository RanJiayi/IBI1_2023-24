import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the file and read the content of it
os.chdir("C:\\Users\\冉嘉忆\\OneDrive - International Campus, Zhejiang University\\桌面\\IBI\\new\\IBI1_2023-24")
dalys_data=pd.read_csv("dalys-rate-from-all-causes")
#ROWS: start from the first row to the 100th row, print every 10th row; COLUMNS: the fourth column
print(dalys_data.iloc[0:101:10,3])
#ROWS: every row where Entity is "Afghanistan"; COLUMNS: the DALYs column
print(dalys_data.loc[dalys_data["Entity"]=="Afghanistan","DALYs"])

#store the data from China in terms of Year and DALYs
interest_columns=[True, False, True, True]
china_data=dalys_data.loc[dalys_data["Entity"]=="China",interest_columns]
#compute the mean DALYs in China
mean_china=np.mean(china_data["DALYs"])
print(mean_china)
#show the value to the DALYs measured for 2019
print(china_data.loc[china_data["Year"]==2019],"DALYs")
#2019 was below the mean according to the output value

#draw the graph
plt.plot(china_data.Year,china_data.DALYs,"yo")
#set the labels and the title
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China over Time")
plt.xticks(china_data.Year,rotation=-90)
#show the graph
plt.show()
plt.clf()

#store the data from the UK
UK_data=dalys_data.loc[dalys_data["Code"]=="GBR",:]
#draw the graph for the data from the UK
plt.plot(UK_data.Year,UK_data.DALYs,"bo",label="UK")
#draw the graph for the data from China
plt.plot(china_data.Year,china_data.DALYs,"yo",label="China")
#set the labels and the title
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China and the UK")
plt.xticks(china_data.Year,rotation=-90)
#show the graph
plt.legend()
plt.show()
plt.clf()