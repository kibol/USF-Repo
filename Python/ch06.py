###1.
##print "produces \nthis \noutput."
##
##
##
###4
##def print_triangular_numbers(endnumb):
##    i = 1  
##    while i <= endnumb:
##       n = i*(i+1)/2
##       print i, '\t', n
##       i += 1
##       
##print_triangular_numbers(5)
##
##
###5
##n >= 2
##def is_prime(x):
##    n = x-1
##    while n > 2:
##        if x%n == 0:
##          print x, " is not a prime number"
##          x -= 1
##        else:
##          print x, "is a prime number"
##        return            
##is_prime (9)

#6.

##def num_digits(n):
##    count=0
##    while n:
##        count = count + 1
##        n = n / 10
##    print count
##
##result = num_digits(0)
##print result

##num-digits(0) returned 0, the initial value of the counter. The condition
##of the while loop was false at the beginning since the argument of 0 not > 0

##def num_digits(n):
##    count = 0
##    while n:
##        count = count + 1
##        n = n / 10
##    return count
##print num_digits(1)

## A call to num_digits (1) will have the program loop once and returna count
## of one. 
##
##def num_digits(n):
##    count = 0
##    while n:
##        count = count + 1
##        n = n / 10
##    return count
##print num_digits(-24)

## A call to num_digits (-24) will result in an infinite. The boolen condition of
## n not zero will not be met.

##7

def num_even_digits(n):
    """
    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """

    count = 0
    while n:
        last_dig = n%10
        if last_dig/2 == 0:
          count += 1
          n = n/10
    return count

print num_even_digits(123456789)


###8 works
##
##def print_digits(n):
##    """
##    >>> print_digits(13789)
##    9 8 7 3 1
##    >>> print_digits(39874613)
##    3 1 6 4 7 8 9 3
##    >>> print_digits(213141)
##    1 4 1 3 1 2
##    """
##
##    while n:
##        last_num = n%10
##        n = n/10
##        print last_num, 
##    
##print_digits(37859)
##
##
###9
##def sum_of_squares_of_digits(n):
##    """
##    >>> sum_of_squares_of_digits(1)
##    1
##    >>> sum_of_squares_of_digits(9)
##    81
##    >>> sum_of_squares_of_digits(11)
##    2
##    >>> sum_of_squares_of_digits(121)
##    6
##    >>> sum_of_squares_of_digits(987)
##    194
##    """
##    result1 = 0
##    while n:
##      new_dig = n%10
##      squared_num = new_dig**2
##      result1 += squared_num
##      n = n/10
##    return result1
##
##print sum_of_squares_of_digits(8567)
##
##

if __name__ == '__main__':
    import doctest
    doctest.testmod()


