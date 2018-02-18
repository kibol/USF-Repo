##def add_matrices(m1, m2):
##    """
##    >>> add_matrices([[1, 2, 3], [4,5,6]], [[2, 3, 4], [3, 4, 5]])
##    [[3, 5, 7], [7, 9, 11]]
##    """
##
##    new_matrix = []
##    for i in range(len(m1)):
##         j_mat = []
##         for j in range(len(m2[0])):
##             j_mat = m1[i][j] + [m2[i][j]
##              result = [j_mat]
##             new_matrix += result
##    return new_matrix


##
##def find(strng, ch):
##    index = 0
##    while index < len(strng):
##        if strng[index] == ch:
##            return index
##        index += 1
##    return -1
##
##print find('hello', 'l')
##
##
##if __name__ == '__main__':
##    import doctest
##    doctest.testmod()

elements = ["xxxxxx", "yyy", "z"]
for element in elements:
    print len(element)
