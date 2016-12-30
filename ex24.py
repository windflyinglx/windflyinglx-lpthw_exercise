#It's a review of almost all we have learnt for now.

print "Let's practicce everything."
#What does slash do in this sentence? Oh yes, if we do not put a slash before ', it would be recognised as the end of the sentence. 
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'


poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-----------------"
print poem
print "-----------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000
#A new way to define variables via a definition
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#A new way to print variables
print "We'd have %d beans, %d jars, %d crateds." % secret_formula(start_point)