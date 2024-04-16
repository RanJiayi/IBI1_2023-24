#create a list to store	the	population sizes for the UK
uk_cities=[0.56,0.62,0.04,9.7]
#sort the population values for the UK
uk_cities.sort()
print('Sorted values for the populations of cities in the UK:',uk_cities)
#create a list to store	the	population sizes for China
chine_cities=[0.58,8.4,29.9,22.2]
#sort the population values for China
chine_cities.sort()
print('Sorted values for the populations of cities in China:',chine_cities)

#Import the graph module
import matplotlib.pyplot as plt
#set the width of two bar plots
width=0.5

#bar plot of the population sizes for the UK
plt.figure()
#set the color
uk_colors = ['rosybrown','salmon','lightcoral','mistyrose']
#set up parameters
uk_cities_index=['Stirling','Edinburgh','Glasgow','London']
plt.bar(uk_cities_index, uk_cities, width, color=uk_colors)
#add title and label descriptions
plt.title('the population sizes for the UK')
plt.ylabel('Population(millions)')
#construct the bar plots
plt.show()
plt.clf()

#bar plot of the population sizes for China
plt.figure()
#set the color
china_colors = ['slateblue','darkslateblue','thistle','plum']
#set up parameters
China_cities_index=['Haining','Hangzhou','Beijing','Shanghai']
plt.bar(China_cities_index, chine_cities, width, color=china_colors)
#add title and label descriptions
plt.title('the population sizes for China')
plt.ylabel('Population(millions)')
#construct the bar plots
plt.show()
plt.clf()