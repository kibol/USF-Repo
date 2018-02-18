
##7
def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
    result= []
    for i in range (len(u)):
        sum_list= [u[i]+v[i]]
        result+= sum_list
    return result    
      
##        
##        
## u=[1,2,3]      v= [4,5,6]      result [5,7,9]
##
## 
##  i             u[i]              v[i]            result
##  0             1                  4               [5]
##  1             2                 `5              [5,7]
##  2             3                  6              [5,7,9]
## 

##8
def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    result =[]
    for elem in v:
        new_list=[elem*s]
        result= result+ new_list
    return result
        

##s= 2            v= [1,2,3]      reuslt  [2, 4,6]
##
##         elem       prod_list     result                                       
##          1  s*1     [2]           [2]
##          2          [4]           [2,4]
##          3          [6]           [2,4,6]

##9
def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    result= 0
    for i in range (len(v)):
        prod = u[i]*v[i]
        result += prod
    return result    

## u=[1,2,3]      v= [4,5,6]      result []
##
##                                             
##  i             u[i]              v[i]       product         result 
##  0             1                  4           4              4
##  1             2                 `5           10             14
##  2             3                  6           18             32
## 

if __name__ == '__main__':
    import doctest
    doctest.testmod()

