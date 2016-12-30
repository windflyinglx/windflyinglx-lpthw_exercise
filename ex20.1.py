#try ex20 again by myself.

from sys import argv

script, input_file = argv

#read the file
def print_all(f):
	print f.read()
	
#rewind the file. I don't know what rewind means.
def rewind_file(f):
	f.seek(0)
	
#print the file
def print_lines(line_count, f):
	print line_count, f.readline()

#give input_file a name	
current_file = open(input_file)

print "First let's print the whole file:"
#it seems a file should be opened, and then can be read.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#Oh, I see the seek()'s meaning. It means go back to the first byte. 
#Because it just types the file once.
print "Let's print three lines:"

count = 1
print_lines(count, current_file)
count += 1
print_lines(count, current_file)
count += 1
print_lines(count, current_file)

