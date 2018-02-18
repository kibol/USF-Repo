##                                # Demba Sissoko
##                                
##import copy
##
##def repeatList(lst, n): 
##    """
##    Returns a new list that is equivalent to lst * n,
##    where * is the repetition operator.
##    Assumes  n is a positive integer.
##    Examples:
##    >>> repeatList(['banana', 'apple', 'orange'], 2)
##    ['banana', 'apple', 'orange', 'banana', 'apple', 'orange']
##    >>> repeatList(['fall', 'winter', 'spring', 'summer'], 1)
##    ['fall', 'winter', 'spring', 'summer']
##    >>> repeatList([1,2,3], 0)
##    []
##    >>> repeatList(['a', 'b', 'c'], 5)
##    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
##    >>> repeatList([['x', 'y', 'z']], 2)
##    [['x', 'y', 'z'], ['x', 'y', 'z']]
##    >>> repeatList([['x', 'y', 'z'], ['a', 'b', 'c']], 2)
##    [['x', 'y', 'z'], ['a', 'b', 'c'], ['x', 'y', 'z'], ['a', 'b', 'c']]
##    >>> repeatList([1, 2, 3], 1)
##    [1, 2, 3]
##    >>> repeatList(['meat', 'fish', 'egg'], 3)
##    ['meat', 'fish', 'egg', 'meat', 'fish', 'egg', 'meat', 'fish', 'egg']
##    >>> repeatList([1, 2, 3, 4, 5, 6, 7], 3)
##    [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
##    >>> repeatList(['red', 'white', 'blue'], 3)
##    ['red', 'white', 'blue', 'red', 'white', 'blue', 'red', 'white', 'blue']
##    """
##    i= 0
##    result= []
##    while i < n:   
##      result += lst
##      i+= 1
##    return result
##
##
##def replace(lst, pos, item): 
##    """
##    Modifies list lst so that its element at pos is replaced with item.
##    Does not modify lst if pos is negative or pos >=  length of lst.
##    Assumes n is an integer.
##    Nothing is returned.
##    Examples:
##    >>> mylist1 = [1, 2, 3]
##    >>> replace(mylist1, 2, 'z')
##    >>> mylist1
##    [1, 2, 'z']
##    >>> mylist2 = [6, 1, 4, 2, 3]
##    >>> replace(mylist2, 5, 'z')
##    >>> mylist2
##    [6, 1, 4, 2, 3]
##    >>> mylist3 = ['a', 'b', 'c', 'd', 'e', 'f']
##    >>> replace(mylist3, 4, 'me')
##    >>> mylist3
##    ['a', 'b', 'c', 'd', 'me', 'f']
##    >>> mylist4 = ['orange', 'appple', 'banana', 'prune', 'quice']
##    >>> replace(mylist4, 3, 'watermelon')
##    >>> mylist4
##    ['orange', 'appple', 'banana', 'watermelon', 'quice']
##    """
##    if pos<0:
##       return
##    elif pos>=len(lst):
##       return
##    lst[pos]= item
##    

def countElem(lst, elem): 
    """
    Returns the number of occurrences of element elem in list lst
    Examples:
    >>> countElem(['a', 'ball', 'a', 'avenue', 'a', 'at',],  'a')
    3
    >>> countElem([1, 3, 1, '123', 1, '1', 1],  1)
    4
    >>> countElem(['abcd', 'abc', 'abc', '123'],  'abc')
    2
    >>> countElem(['w', 'owl', 'w', 'awesome', 'w'],  'w')
    3
    >>> countElem(['mat', 'mate', 'map', 'mapping'],  'map')
    1
    >>> countElem([[1,2,3], '123', 123, [1,2,3], [1,2,3]], [1,2,3])
    3
    """
    count=0
    for i in lst:
        if i== elem:
           count+=1
    return count


##
##def findLast(lst, elem): 
##    """
##    Returns the index of the last occurrence of element elem in list lst or -1 if elem does not occur in lst.
##    Examples:
##    >>> findLast([145, 'abc', '145', '154', [1, 4, 5]],  145)
##    0
##    >>> findLast(['w', 'owl', 'w', 'awesome', 'w'],  'w')
##    4
##    >>> findLast(['a', 'b', 'c', 'c', 'circle'],  'c')
##    3
##    >>> findLast([1, '1', 11, 'none', '1', 1],  1)
##    5
##    >>> findLast([1, [1, 1, 1, 1], [1, 1, 1, 1], 'one', [1, 1, 1, 1]],  [1, 1, 1, 1])
##    4
##    """
##    
##    result = -1
##    for i in range(len(lst)):     
##        if lst[i] == elem:
##           result = i
##    return result
##
##
##def string2list(s): 
##    """
##    Returns a list whose elements are each of the characters in string s as ordered in s
##    Examples:
##    >>> string2list('cat')
##    ['c', 'a', 't']
##    >>> string2list('apple')
##    ['a', 'p', 'p', 'l', 'e']
##    >>> string2list('dog')
##    ['d', 'o', 'g']
##    >>> string2list('pet')
##    ['p', 'e', 't']
##    >>> string2list('elevator')
##    ['e', 'l', 'e', 'v', 'a', 't', 'o', 'r']
##    """
##    result= []
##    for elm in s:
##        result+= elm
##    return result                    
##    
##
##
##def lastOccurMostFreqElem(lst):
##    """
##    Returns the index of the last occurrence of the element that most frequently occurs in list lst
##    or -1 if lst is empty. If elements occur with equal frequency, returns index of the last of these.
##    Examples:
##    >>> lastOccurMostFreqElem([0,0,2,2,0,2])
##    5
##    >>> lastOccurMostFreqElem([3,5,5,5,5,3,5])
##    6
##    >>> lastOccurMostFreqElem([2,3,2,2,3,2,2])
##    6
##    >>> lastOccurMostFreqElem([3,3,2,2,3])
##    4
##    >>> lastOccurMostFreqElem([0,0,2,0,2,0,0,0])
##    7
##    >>> lastOccurMostFreqElem([2,2,2,3,2,2,3])
##    5
##    >>> lastOccurMostFreqElem([3,2,2,3])
##    3
##    >>> lastOccurMostFreqElem([])
##    -1
##    """
##    mostFreqIndex = 0
##    if len(lst)==0:
##      return -1
##    for i in range(len(lst)):
##        if countElem(lst, lst[i])>= countElem(lst, lst[mostFreqIndex]):
##           mostFreqIndex= i
##    return mostFreqIndex
##
##
##
##def insert(s1, s2, pos): 
##    """
##    Returns a new string that is equivalent to string s1 with string s2 inserted at index pos.
##    Returns empty string if pos is negative or pos >  length of s1.
##    Assumes n is an integer.
##    Examples:
##    >>> insert('', 'world!', 0)
##    'world!'
##    >>> insert('world', 's', 2)
##    'wosrld'
##    >>> insert('world', 's', 5)
##    'worlds'
##    >>> insert('needy', 'r', 2)
##    'neredy'
##    >>> insert('word!', 's', 0)
##    'sword!'
##    >>> insert('word', 'l', 3)
##    'world'
##    >>> insert('a!', 'live', 1)
##    'alive!'
##    """
##    new_string=''      
##    if pos > len(s1) or pos < 0:
##      return ''
##    if len(s1)== pos:
##      return s1 + s2
##    for i in range(len(s1)):
##        if i != pos:
##           new_string += s1[i]
##        else:
##           new_string= new_string + s2 + s1[i]
##    return new_string
##        
##
##def substring(s, pos1, pos2): 
##    """
##    Returns a new string consisting of the characters of string s from pos1 to pos2-1 inclusive.
##    Returns the empty string if there is no valid substring beginning at pos1 and ending at pos2-1.
##    Assumes both pos1 and pos2 are integers.      
##    Examples:
##    >>> substring('cat', 1, 3)
##    'at'
##    >>> substring('pineapple', 4, 9)
##    'apple'
##    >>> substring('revolution', 1, 10)
##    'evolution'
##    >>> substring('revolt', 2, 6)
##    'volt'
##    >>> substring('ozone', 1, 5)
##    'zone'
##    """
##           
##    new_string= ""       
##    i = pos1
##    while i < pos2:
##         new_string+= s[i]
##         i += 1
##    return new_string
##
##
##def str2int(s): 
##    """
##    Returns an integer that is the integer equivalent of the string s.
##    Assumes that s is the string version of a valid integer.
##    Examples:
##    >>> str2int('1000092')
##    1000092
##    >>> str2int('-1000092')
##    -1000092
##    >>> str2int('245000')
##    245000
##    >>> str2int('0')
##    0
##    >>> str2int('-12050450')
##    -12050450
##    >>> str2int('-1')
##    -1
##    >>> str2int('1111')
##    1111
##    """
##    sign=1 
##    i=0
##    if s[0]=="-":
##       i= 1
##       sign=-1
##    elif s=='0':
##       return 0
##    else:
##       sign=1
##    result=0   
##    while i < len(s):
##       dig= ord(s[i])-48
##       result= dig + result*10
##       i+=1
##    return result*sign
##
##
##def int2str(i): 
##    """
##    Returns a string that is the string equivalent of valid integer i
##    Examples:
##    >>> int2str(-1000092)
##    '-1000092'
##    >>> int2str(-123124)
##    '-123124'
##    >>> int2str(1000092)
##    '1000092'
##    >>> int2str(0)
##    '0'
##    >>> int2str(-10)
##    '-10'
##    >>> int2str(1)
##    '1'
##    >>> int2str(-123)
##    '-123'
##    >>> int2str(-2)
##    '-2'
##    """
##    sign='-'
##    result=''
##    if i<0:
##      i=i*-1
##    elif i == 0:
##      return "0"
##    else:
##      sign=''
##    while i>0: 
##         dig = i%10
##         result = chr(dig+48)+ result
##         i = i/10
##    return sign + result
##      
##
##
##if __name__ =='__main__':
##    import doctest
##    doctest.testmod()
##
