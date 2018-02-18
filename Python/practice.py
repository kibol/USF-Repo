##### x**3 - y/x
##
##def compute(x,y,z):
##    return x**3 - y/z
##

##print compute(2,12,3)
##x= 3
##y= 12
##print compute (10,25,200)
##
##
##a = raw_input(" Please enter your 2 names: ")
####print a
##
##b = raw_input(" Give me 4 nouns: ")
##print b
##
##c = raw_input(" Enter 4 verbs: ")
##print c
##
##d = raw_input(" Give 2 adverbs: ")
##print d
##
##e = raw_input(" Please enter 3 adjectives: ")
##print e
##
##f = raw_input(" Please name two friends: ")
##print f
##
##g = raw_input(" Please provide 2 past tense verbs: ")
##print g
##
##print a, b, c, d, e, f, g

##print "First Line."
##new_line()
##print "Second Line."

##def new_line():
##    print 100**10
##
##print "First Line"
##new_line()
##print "Second Line"
##
##def three_lines():
##    new_line()
##    new_line()
##    new_line()
##
##print "First Line"
##three_lines()
##print "Second Line"
##
##
### Note.  The reason we could even call three_lines is because new_line was defined
### first.  Therefore, three_lines is dependent on new_line.
##
##
##
##def cat_twice(part1, part2):
##    cat = part1 + part2
##    print_twice(cat)

##chant1 = "Pie Jesu domine, "
##chant2 = "Dona eis requiem."
##cat_twice(chant1, chant2)    
##
##

##
##def print_square_root(x):
##    if x <= 0:
##        print "Positive numbers only, please."
##        return
##
##    result = x**0.5
##    print "The square root of", x, "is", result
##
##print_square_root(81)
##print_square_root(2500)

 ################################################################

#Chapter 5


##def distance(x1, y1, x2, y2):
##    dx = x2 - x1
##    dy = y2 - y1
##    print "dx is", dx
##    print "dy is", dy
##    return 0.0
##
##
##def distance(x1, y1, x2, y2):
##    dx = x2 - x1
##    dy = y2 - y1
##    dsquared = dx**2 + dy**2
##    result = dsquared**0.5
##    return result
##def distance(3,4,5,0):

##
##def f(n):
##    return 3*n - 6
##
##def g(n):
##    return 5*n + 2
##
##def h(n):
##    return -2*n + 17
##
##def doto(value, func):
##    return func(value)
##
##print doto(7, f)
##print doto(7, g)
##print doto(7, h)
##


##def seven_digits(x):
##    
##    mil= x/1000000
##    print mil 
##
##    thou= (x/1000)%1000
##    print thou
##
##    ones= x%1000
##    print ones
##
##    print str(mil)+','+ str(thou)+','+str(ones)
##
##seven_digits(123456789)

##def absolute_value(x):
##    if x < 0:
##        return -x
##    elif x > 0:
##        return x
##
##absolute_value(-6)
##

##def distance(x1, y1, x2, y2):
##    dx = x2 - x1
##    dy = y2 - y1
##    dsquared = dx**2 + dy**2
##    result = dsquared**0.5
##    return result
##
##distance (1,2,4,6)
##
##



# Module 6


##def sequence(n):
##    while n != 1:
##        print n,
##        if n % 2 == 0:      
##            n = n / 2
##        else:                 
##            n = n * 3 + 1
##
##sequence (3)

##def num_digits(n):
##    count = 0
##    while n:
##        count = count + 1
##        n = n / 10
##    return count
##
##num_digits (710)
####
##
##def absolute_value(x):
##    if x < 0:
##        return -x
##    else:
##        return x
##
##absolute_value (-80)
##
##



