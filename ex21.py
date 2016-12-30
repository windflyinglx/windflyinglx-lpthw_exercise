#return something after using a function

def add(a, b):
	print "Adding %r + %r" % (a, b)
	return a + b
	
def substract(a, b):
	print "substrcting %r - %r" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %r * %r" % (a, b)
	return a * b

def divide(a, b):
	print "dividing %r / %r" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
IQ = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, IQ)
#Learn a new way to demonstrate variables
print "Age: ", age, "Height: ", height, "Weight: ", weight, "IQ: ", IQ

print "Here is a puzzle"

what_is_it = add(age, substract(height, multiply(weight, divide(IQ, 2))))

#Why don't I need to put %r here? But just a variable's name?
print "That becomes ", what_is_it, "Can you do it by hand?" 
             