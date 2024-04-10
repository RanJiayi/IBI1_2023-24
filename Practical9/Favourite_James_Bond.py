#James Bond actor and their corresponding years
Bond_films={1973:"Roger Moore",1987:"Timothy Dalton",1995:"Pierce Brosnan",2006:"Daniel Craig"}
actor_year=[1973,1987,1995,2006]
def Bond_dates(age):
	#calculate the year when the individual started watching Bond films
	start_year=2024-age+18
	#find the most recent movie release year before the individual started watching Bond films
	for i in range(len(actor_year)):
		if actor_year[i]<start_year:
			film_year=actor_year[i]
	#output the actor's name that corresponds to the year
	favorite_Bond=Bond_films[film_year]
	return favorite_Bond

age=int(input("Age of the individual:"))
#call function
print(Bond_dates(age))
	