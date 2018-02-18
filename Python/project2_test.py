def countElem(lst, elem):

    """
    Returns the number of occurrences of element elem in list lst
    Examples:
    >>> countElem(['w', 'owl', 'w', 'awesome'],  'w')
    2
    """
    count=0
    for i in lst:
       if i==elem:
        count+=1
    return count  
 
print countElem(['w', 'owl', 'w', 'w', 'awesome'],  'w')
