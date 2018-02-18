##5
def reverse(s):
     """
       >>> reverse('happy')
       'yppah'
       >>> reverse('Python')
       'nohtyP'
       >>> reverse("")
       ''
       >>> reverse("P")
       'P'
     """
     result= ""
     for char in s:
       result = char + result
     return result



##6
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror('')
      ''
      >>> mirror("a")
      'aa'
    """

    result1 = ""
    for char in s:
       result1 = char + result1
    result2= ""
    for char in s:   
       result2 = result2 + char
    return result2+result1

##7
def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """

    result = ""
    for char in strng:
        if char != letter:
          result = result + char
    return result 

##8
def is_palindrome(s):

      """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
      """

      i1 = 0
      i2 = -1
      i = 0
      while i < len(s)/2:      
        if s[i1] == s[i2]: 
           i1 += 1
           i2 -= 1
           i  += 1
        else:
          return False
      return True  
        

def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    
    i1 = 0
    i2 = len(sub)
    count = 0
    while i1 < len(s):
        if s[i1:i2 ] == sub:
           count += 1
        i1 += 1
        i2 += 1 
    return count  
           
s= "an"
sub = "banana"
i = count(sub, s)


def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    start = 0
    end = len(sub)
    result = ""
    while start < len(s):
        if s[start:end]!= sub:
           result = result + s[start]  
           start += 1
           end += 1
        else:
            result= result+ s[end:]
            return result
    return result
print remove ("nana", "banana")

def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    start = 0
    end = len(sub)
    result =""
    while start< len(s): 
        if s[start:end]!= sub:
           result = result + s[start]  
           start += 1
           end += 1
        else:
           start += len(sub)
           end += len(sub)
    return result       

print remove_all ("iss", "mississippi")



if __name__ == '__main__':
    import doctest
    doctest.testmod()
