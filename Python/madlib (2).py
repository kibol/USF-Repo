# 1.

# print n = 7
# Error message== There is an error in your program: invalid syntax

print 7 + 5

##print 5.2, "this", 4-2,"that", 5/2.0
## #Error message== There is an error in your program: invalid syntax
## print statement only works if a correct syntax is entered
### In this case it returned an error message.
##
### 2.

a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy"

print a,  b,  c,  d,  e,  f,  g,  h,  i

# 3.

print(6 * 1) - 2

# When I put a comment # symbol in front (6*1)-2 the code did not get executed in Shell.


# 5.

x = input()
3.14
type (x)

# I received the following error message:
#Traceback (most recent call last):
#File "C:\Users\Demba\Desktop\D File\USF\HS 608\madlib.py", line 38, in <module>
#x = input()
#File "<string>", line 1
# x = input()
#SyntaxError: invalid syntax

x = raw_input()
3.14
type (x)

# The interpreter did not return any value.

x = input()
'the knights who say "ni!"'
type (x)

# Received the follwoing error message: SyntacxError: invalid syntax

x = input()
#the knights who say "ni!"
type (x)

# The interpreter returned the follwong error: Traceback (most recent call last):
#File "<pyshell#5>", line 1, in <module>
#x = input()
#File "<string>", line 1
#the knights who say "ni!"              ^
#SyntaxError: invalid syntax


x = raw_input()
#the knights who say "ni!"
type (x)

# Shell returned no value, started a new code line.

# 6.

# bruce + 4 was run and i received the following message:
#Traceback (most recent call last):
#File "<pyshell#11>", line 1, in <module>
#bruce+4
#NameError: name 'bruce' is not defined

# When bruce was assigned a value of 6; result was 10.
#>>> bruce= 6
#>>> bruce+4
#10

# 7.

a = raw_input(" Please enter your 2 names: ")
print a

b = raw_input(" Give me 4 nouns: ")
print b

c = raw_input(" Enter 4 verbs: ")
print c

d = raw_input(" Give 2 adverbs: ")
print d

e = raw_input(" Please enter 3 adjectives: ")
print e

f = raw_input(" Please name two friends: ")
print f

g = raw_input(" Please provide 2 past tense verbs: ")
print g

print a, b, c, d, e, f, g

