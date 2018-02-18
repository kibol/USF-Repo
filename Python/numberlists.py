##15

def only_evens(numbers):
    """
      >>> only_evens([1, 3, 4, 6, 7, 8])
      [4, 6, 8]
      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 0]
      >>> only_evens([1, 3, 5, 7, 9, 11])
      []
      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
      [4, 0, 2, 6, -4]
      >>> nums = [1, 2, 3, 4]
      >>> only_evens(nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    result= []
    for elm in numbers:
       if elm%2 == 0:
         result += [elm]
    return result
       
      
def only_odds(numbers):
    """
      >>> only_odds([1, 3, 4, 6, 7, 8])
      [1, 3, 7]
      >>> only_odds([2, 4, 6, 8, 10, 11])
      [11]
      >>> only_odds([1, 3, 5, 7, 9, 11])
      [1, 3, 5, 7, 9, 11]
      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
      [-1, 7]
      >>> nums = [1, 2, 3, 4]
      >>> only_odds(nums)
      [1, 3]
      >>> nums
      [1, 2, 3, 4]
    """
    result= []
    for elm in numbers:
       if elm%2 != 0:
         result += [elm]
    return result
       

##16

def multiples_of(num, numlist):
    """
    >>> multiples_of(3, [1, 3, 4, 6, 7, 8, 12])
    [3, 6, 12]
    >>> multiples_of(2, [1, 2, 4, 6, 7, 8, 10])
    [2, 4, 6, 8, 10]
    >>> multiples_of(5, [1, 5, 15, 10 , 8])
    [5, 15, 10]
    >>> multiples_of(7, [14, 3, 21, 6, 7, 28])
    [14, 21, 7, 28]
    """
    result=[]
    for elm in numlist:
       if elm%num==0:
         result+=[elm]
    return result

       
if __name__ == '__main__':
    import doctest
    doctest.testmod()
      
                






















