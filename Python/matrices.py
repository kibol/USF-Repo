import copy

##11

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
    for i in range(len(u)):
        sum_list= [u[i]+v[i]]
        result+= sum_list
    return result


def scalar_mult_v(s, v):
    """
      >>> scalar_mult_v(5, [1, 2])
      [5, 10]
      >>> scalar_mult_v(3, [1, 0, -1])
      [3, 0, -3]
    """
    result =[]
    for elem in v:
        new_list=[elem*s]
        result= result+ new_list
    return result

        

def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """

    matrix_clone = copy.deepcopy(matrix)
    num_col= len(matrix[0])
    y = [[0]*num_col]
    result= matrix_clone + y
    return result


def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    result=[]
    for elm in matrix:
      new_matrix = [elm + [0]]
      result += new_matrix
    return result   


##12
def add_matrices(m1, m2):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[2, 2], [2, 2]]
    >>> add_matrices(a, b)
    [[3, 4], [5, 6]]
    >>> c = [[8, 2], [3, 4], [5, 7]]
    >>> d = [[3, 2], [9, 2], [10, 12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    >>> d
    [[3, 2], [9, 2], [10, 12]]
    """
    i=0
    result=[]
    while i < len(m1):
        new_row= add_vectors (m1[i],m2[i])       
        new_matrix= [new_row]
        result+= new_matrix
        i += 1
    return result


##13
def scalar_mult(s, m):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> scalar_mult(3, a)
    [[3, 6], [9, 12]]
    >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    >>> scalar_mult(10, b)
    [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
    >>> b
    [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    i=0
    result=[]
    while i < len(m):
        new_row = scalar_mult_v(s, m[i])
        result+= [new_row]
        i+= 1
    return result

##14

def row_times_column(m1, row, m2, column):
    """
    >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
    19
    >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
    22
    >>> row_times_column([[1, 2, 5], [3, 4, 6]], 1, [[5, 6], [7, 8],[1, 1]], 0)
    49
    >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
    50
    """
    result=0
    for i in range(len(m1[0])):
      result+=m1[row][i]*m2[i][column]
    return result
    

def matrix_mult(m1, m2):
    """
    >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    result= []
    for i in range(len(m1)):
       row= []
       for j in range(len(m2[0])):
         row += [row_times_column(m1,i,m2,j)]
       result+= [row]
    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()

