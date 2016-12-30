#define a function

def print_two(*args):
	arg1, arg2 = args
	print "arg1 = %r, arg2 = %r" % (arg1, arg2)
	
def print_twoAgain(arg1, arg2):
	print "arg1 = %r, arg2 = %r" % (arg1, arg2)
	
def print_one(arg):
	print "arg1 = %r" % arg
	
def print_none():
	print "I got nothin'."
	
	
print_two("Zed", "Shaw")
print_twoAgain("Zed", "Shaw")
print_one("First!")
print_none()