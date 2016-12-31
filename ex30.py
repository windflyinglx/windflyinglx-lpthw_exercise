#if and elif and else

people = 30
trucks = 15
cars = 40

if people < cars:
	print "We should take the cars."
elif people > cars:
	print "Cars should take us."
else:
	print "Either would be Ok."
	
if trucks > cars:
	print "Trucks are more than cars."
elif cars > trucks:
	print "Cars are more than trucks."
else:
	print "They are equal."

if people > trucks:
	print "People are going to eat trucks."
elif trucks > people:
	print "Trucks will create much smog."
else:
	print "Every one should have a truck!"
