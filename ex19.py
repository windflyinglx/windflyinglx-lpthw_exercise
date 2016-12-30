#variables and define a function

# use function via give the number directly
def cheese_and_crackers(cheese_count, the_box_of_crackers):
	print "You have %r cheeses!" % cheese_count
	print "You have %r boxes of crackers!" % the_box_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
cheese_and_crackers(20,30)

# use function via variables
print "OR, we can use variables from out script:"
cheeseAmount = 20
crackersAmount = 30
cheese_and_crackers(cheeseAmount, crackersAmount)

# do math inside the funtion

cheese_and_crackers(15+5, 20+10)

# combine variables and math together

print "And we can combine the two, variables and math;"
cheese_and_crackers(90+cheeseAmount, 1020+crackersAmount)
