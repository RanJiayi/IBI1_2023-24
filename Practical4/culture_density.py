#day 1
n=1
#at 5% density
x=5
#repeat until the density passes 90%
while x<90:
#the cell line doubles in density everyday
	x=x*2
#the number of days increase by one everyday
	n=n+1
print(f"On day {str(n)} the cell density goes over 90%.")
