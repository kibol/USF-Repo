# 1.

##>>> 5%2
##1
##>>> 9%5
##4
##>>> 15%12
##3
##>>> 6%6
##0
##>>> 0%7
##0
##>>> 7%0
##
## Traceback (most recent call last):
## File "<pyshell#14>", line 1, in <module> 7%0
## ZeroDivisionError: integer division or modulo by zero
## Since division by zero is not possible, python can't give a remainder. Thus the
## error message 


# 2.

def compare (x,y):

    if x < y:
       print x, "is less than", y
    elif x > y:
       print x, "is greater than", y
    else:
       print x, "and", y, "are equal"

compare (3,9)
compare (6,1) 
compare ((3*2),(4+2))

# 4.

##>>> True or False
##True
##>>> True and False
##False
##>>> not(False) and True
##True
##>>> True or 7
##True
##>>> False or 7
##7
##>>> True and 0
##0
##>>> False or 8
##8
##>>> "happy" and "sad"
##'sad'
##>>> "happy" or "sad"
##'happy'
##>>> "" and "sad"
##''
##>>> "happy" and ""
##''


##Integers and floats will evaluate to True except for zero. Strings will evaluste to
##false except for when the string is empty.  For boolean values the True is True and False
##is False.  For boolean expressions involving an "or", at least one of the operands has to be true
## true; for boolean expressions involving an "and" both operands have to be true. 
## The operator "not" will change any boolean expression to the opposite. 
################################################################################
 

# 5.

def function_a():
    print "function_a was called..."

def function_b():
    print "function_b was called..."

def function_c():
    print "function_c was called..."

def dispatch (choice):
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print "Invalid choice."

ch = raw_input (" Please enter a,b or c: ")

dispatch (ch)


# 6.


def is_divisible_by_3(x):

    if not 0 < x < 10:
         print "Invalid entry! Single digit, positive number only please"
         return
    
    else:

         if x % 3 == 0:
            print x, " is divisible by 3" 

         else:
            print x, "is not divisible by 3"          

is_divisible_by_3 (6)

def is_divisible_by_5(x):

    if not (0 < x < 10):
         print "Invalid entry! Single digit, positive number only "
         return
    
    else:

         if x % 5 == 0:
            print x, " is divisible by 5" 

         else:
            print x, "is not divisible by 5"       

is_divisible_by_5 (10)


# 7.

def is_divisible_by_n(x,y):

    if x%y==0:
        print x, "is divisible by", y

    else:
        print x, "is not divisible by", y

is_divisible_by_n(43,9)


