# the method write() and open(filename, 'w')
# the largest fine we have learnt.


from sys import argv

script, filename = argv
 
print "We are going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."
 
raw_input("?")
 
print "Opening the file..."
print "Trunacting the file. Goodbye!"
filework = open(filename, 'w')
filework.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("Line1:")
line2 = raw_input("Line2:")
line3 = raw_input("Line3:")
print "I'm going to write these to the file."
filework.write(line1)
filework.write("\n")
filework.write(line2)
filework.write("\n")
filework.write(line3)
filework.write("\n")
print "And finally, we close it."
filework.close()