#starting at day 1
day=1
#starting at 5% density
density=5
#repeat until the density passes 90%
while density<90:
#the cell line doubles in density everyday
	density=density*2
#the number of days increase by one everyday
	day=day+1
#the maximum number of days for holiday = the number of days before the cell density passes 90
day_holiday=day-1
print(f"On day {str(day)} the cell density goes over 90%, and the maximum number of days for holiday is {str(day_holiday)}.")