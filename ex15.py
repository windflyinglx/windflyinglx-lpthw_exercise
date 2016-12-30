# the method read() and the command open

from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r" % script
print txt.read()

print "Type the filename again."
name = raw_input(">")
openit = open(name)
print openit.read()
