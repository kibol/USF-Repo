# 1.

def compare (a, b):
    """
      >>> compare(5, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 3)
      -1
      >>> compare(42, 1)
      1
    """
    
    if a > b:
      return 1

    elif a==b:
      return 0

    else:
      return -1

#2. 

def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """

    h = (a**2 + b**2)**0.5
    return h


#3.

def distance(x1, y1, x2, y2):
    chx = x2 - x1
    chy = y2 - y1
    d = (chx**2 + chy**2)**0.5
    return d


def slope (x1, y1, x2, y2):
    """
       >>> slope(5, 3, 4, 2)
       1.0
       >>> slope(1, 2, 3, 2)
       0.0
       >>> slope(1, 2, 3, 3)
       0.5
       >>> slope(2, 4, 1, 2)
       2.0
    """
    chx = x2 - x1
    chy = y2 - y1
    chcomp = chy/float(chx)
    return chcomp


def intercept(x1, y1, x2, y2):
    """
       >>> intercept(1, 6, 3, 12)
       3.0
       >>> intercept(6, 1, 1, 6)
       7.0
       >>> intercept(4, 6, 12, 8)
       5.0
    """

    polys = slope (x1, x2, x3, x4)
    b = y1 - polys * x1 
    return b    

#4.

def is_even(n):
    """
     >>> is_even(8)
     True
     >>> is_even(9)
     False
    """

    if n%2 == 0:
       return True

    else:
        return False      

#5.
     
def is_odd(n):
    """
      >>> is_odd(8)
      False
      >>> is_odd(9)
      True
    """

    if n%2 != 0:
       return True

    else:
        return False

def is_odd2(n):
    """
      >>> not is_even(9)
      True
      >>> not is_even(8)
      False
    """
    if n%2== 1:
        return True

    else:
        return False


#6.

def is_factor(f,n):
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    if n%f == 0:
       return True
    
    else:   
       return False

#7.

def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """

    if m%n == 0:
       return True
    else:
       return False


        
if __name__ == '__main__':
    import doctest
    doctest.testmod()

  
