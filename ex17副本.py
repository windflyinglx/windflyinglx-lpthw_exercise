#import more file. 
#copy from a file to another
#also learn the usage of echo(create a file) and cat (stream line)

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %r" % (from_file, to_file)

#We can use semicolon to combine the code to one line.
copy = open(from_file); copyfile = copy.read()

#copyfile = open(from_file, 'r')

print "The input file is %r bytes long." % len(copyfile)

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."

tofile = open(to_file, 'w')
to_file = tofile.write(copyfile)

print "Alright, all done."

#I cannot figure out which file should be closed.
#Now I figure out. The file that was open before should be closed.
tofile.close()
copy.close()
