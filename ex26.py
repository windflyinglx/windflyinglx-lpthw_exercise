#add print for all of the """
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#rectify words.poop(0) into words.pop(0)  BTW, that's hilarious!
#change def print_first_word(words) into def print_first_word(words):
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

#add an ) for word = words.pop(-1
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# change it into print "This should be five: %s" / five
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#change jars = jelly_beans \ 1000 into jars = jelly_beans / 1000
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#it should be = rather than ==, and the variable should be start_point rather than start-point
beans, jars, crates = secret_formula(start_point)

#It should be beans rather than jeans... You must be kidding me!
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

#the method behind the % should be secret_formula(start_point)
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

#change \t into t\ 
sentence = "All good things come to those who weight."

#I think it should be words = break_words(sentence) rather than words = ex25.break_words(sentence)
words = break_words(sentence)
print "This is break_words(sentence)"
sorted_words = sort_words(words)
print "This is sort_words(words)"

# change .print_first_word(sorted_words) into print_first_word(sorted_words)
# change prin sorted_words into print sorted_words
# change sorted_words = ex25.sort_sentence(sentence) into sorted_words = sort_sentence(sentence)
print_first_word(words)
print "first_word(words)"
print_last_word(words)
print "last_word(words)"
print_first_word(sorted_words)
print "first_word(sorted_words)"
print_last_word(sorted_words)
print "last_word(sorted_words)"
sorted_words = sort_sentence(sentence)
print "sort_sentence(sentence)"
print sorted_words
print "sorted_words"

#change print_irst_and_last(sentence) into print_first_and_last(sentence)
#change print_first_a_last_sorted(senence) into print_first_and_last_sorted(sentence), with no indent
print_first_and_last(sentence)
print "first_and_last(sentence)"

print_first_and_last_sorted(sentence)
print "first_and_last_sorted(sentence)"
