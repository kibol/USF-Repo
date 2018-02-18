#9
def num_list(lst, num):
    new_lst = []
    for elem in lst:
      new_lst += [elem*num]
    return new_lst

my_list = [1,2,3]
my_num = 3

print num_list(my_list, my_num)

#10

def pos_int(lst, val):
    new_lst = []
    for elem in lst:
      if val%elem == 0:
        new_lst += [elem]
    return new_lst    
        
my_list = [1,2,3,4,5,6,8]
val = 12
print pos_int(my_list, val)


#11
def modify_element(lst,i,item):
  if i <0:
    return 
  elif i > len(lst):
    return  
  lst[i] = item


my_list = [1,2,3]
i= 1
item= 100

print modify_element(my_list,i,item)
 
#12
#a

def get_elements(lst, start, end):
    result =[]
    i = start
    while i <= end:
       result += [lst[i]]
       i += 1
    return result  


my_list = [5,8,4,3,99]

print get_elements(my_list, 1, 3)

#b

lst = [5,8,4,3,99,5,100,9,6,4,9]

alpha = input("Please enter an integer as a start ")
omega = input("Please enter an integer as an end ")
sub = get_elements(lst, alpha, omega)
print sub    

#13

def avg_ith_row(mat,i):
    result= 0
    for j in range(len(mat[i])):
        result += mat[i][j]
    return result / len(mat[i])
        
my_mat = [[5,8,4],[3,99,5],[30,9,6],[3,4,9]]        
mat_idx = 2

print avg_ith_row(my_mat, mat_idx)

#14

def standardize_row(mat, i):
    new_list = []
    aver_lst = avg_ith_row(mat,i)
    for elm in mat[i]:
      new_list += [elm - aver_lst]
    return new_list

my_mat = [[5,8,4],[3,99,5],[30,9,6],[3,4,9]]

i = 2
print standardize_row(my_mat, i)


#15
def standardize_matrix(mat):
    
    new_std_mat=[]
    for i in range(len(mat)):
       new_std_mat += [standardize_row(mat, i)]
    return new_std_mat    
    
my_mat = [[5,8,4],[3,99,5],[30,9,6],[3,4,9]]
print standardize_matrix(my_mat)


##def func (lst):
##     w = 0
##     for i in range(len(lst)):
##          if  lst[i] < lst[w]:
##              w =  i
##              print i, lst[i],lst[w], 
##     return w
