#n:the number of days; day 1
n=1
#x:cell density; at 5% density
x=5
#repeat until the density passes 90%
while x<90:
#the cell line doubles in density everyday
	x=x*2
#the number of days increase by one everyday
	n=n+1
#the maximum number of days for holiday = the number of days before the cell density passes 90
m=n-1
print(f"On day {str(n)} the cell density goes over 90%, and the maximum number of days for holiday is {str(m)}.")
