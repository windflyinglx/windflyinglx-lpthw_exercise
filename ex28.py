#logical boolean practice

True and True
print "True\n"

False and True
print "False\n"

1 == 1 and 2 == 1
print "False\n"

"test" == "test"
print "True\n"

1 == 1 or 2 != 1
print "True\n"

True and 1 == 1
print "True\n"

False and 0 != 0
print "False"

True or 1 == 1
print "True"

"test" == "testing"
print "False"

1 != 0 and 2 == 1
print "False"

"test" != "testing"
print "True"

"test" == 1
print "False"

not (True and False)
print "True"

not (1 == 1 and 0 != 1)
print "False"

not (10 == 1 or 1000 == 1000)
print "False"

not (1 != 10 or 3 == 4)
print "False"

not ("testing" == "testing" and "Zed" == "Cool Guy")
print "True"

1 == 1 and (not ("testing" == 1 or 1 == 0))
print "True"

"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print "False"

3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print "False"
