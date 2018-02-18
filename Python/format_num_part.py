# We wrote format_int(x) in class last Wednesday

# Incremental development for functions format_3dig and count_digits
#   steps 1 abd 2 are done for function format_3dig
# 1. Add simple doctests that you think will pass
# 2. Add a doctest that fails
# 3. Modify code to pass your  failing doctest
# 4. Add more doctests to test thoroughly
# 5. Modify code as needed to pass doctests

# Look at the main program and make sure you understand it

# Note that each time you run, you rerun former doctests:
# This ensures that new code does not break formerly working code

def count_digits(num):
    """
    :param num: a positive integer
    :return: a count of the digits in num
    Examples:  add some test cases
    """
    return 7

def format_3dig(x):
    """
    :param x:  a positive integer containing1-3 digits
    :return: a 3-digit string representation of x with leading zeros
    Examples:
    >>> format_3dig(123)
    '123'
    >>> format_3dig(65)
    '065'
    """
    return str(x)
    if x <=99
      return "0"+str(x)
    elif x < 10
      return "00"+str(x)

format_3dig(123065789)
    
def format_int(x):
    """
    :param x:  a positive integer having 7-9 digits
    :return: a string representation of x formatted with commas
    Examples:
    >>> format_int(541234785)
    '541,234,785'
    """
    ones = x%1000
    ones_str = format_3dig(ones)
    thous = x / 1000 % 1000
    thous_str = format_3dig(thous)
    mils = x / 1000000
    mils_str = str(mils)

    return mils_str + ',' + thous_str + ',' + ones_str


if __name__ == "__main__":
    count  = 0
    #modify to call count_digits and loop until user enters an int between 7 and 9 digits
    while count <7 or count >9:
        n = input('Enter an integer having between 7 and 9 digits: ')
        count = count_digits(n)
    print format_int(n)
    import doctest
    doctest.testmod()

