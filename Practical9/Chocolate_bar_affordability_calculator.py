def  Chocolate_bar(total_money,price):
	#calculate the number of bars and left change
	number=total_money//price
	change=total_money%price
	return number,change
#input the total money and the unit price
total_money=int(input('The total money you have:'))
price=int(input('The price of one chocolate bar:'))
#call function
output=Chocolate_bar(total_money,price)
print(f"{output[0]} chocolate bar(s) can be bought and {output[1]} will be left over.")