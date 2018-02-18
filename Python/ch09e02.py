##2
my_list = ['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'],[1,2,3]]
## Received the following error with 1 as part the list
##TypeError: object of type 'int' has no len()
for elem in my_list:
     print len(elem)



# Received the follwing error message: TypeError: object of type 'int' has no len()
##my_list[1:1]= ["one"]
##print len(elem)


##4
a = [1,2,3]
b = a[:]
print a
print b
# a=[1,2,3]
# b= [1,2,3]
b[0] = 5
# a= [1,2,3]
# b= [5,2,3]
print a
print b

###17

##string.split and string.join have an inverse relationship. string.split
##change a string of characters into its indidual compoment.  string.join will
##take a list and reverse it into into string. Used togetther as in string.split(string.join())
##there is no effect because the original string is reverted to what it was before applying the
##module.##By default both of these modules will split or join at white spaces. However, they could be
##be set to split or join at a specified location inside a string or a list, making them ideal for inserting
## substrings.


##18

import string

def replace(s, old, new):
    """
      >>> replace('Mississippi',  'i', 'I')
      'MIssIssIppI'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
      >>> replace(s, 'om', 'am')
      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    split_list =string.split(s, old)
    result=string.join(split_list, new)
    return result

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'

print replace(s, 'om', 'am')
           
if __name__ == '__main__':
    import doctest
    doctest.testmod()








    

    
