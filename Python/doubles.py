# modifieer returs nothing, modfies the list to double every element

def doubles2 (lst):
    result=[]
    for i in range(len(lst)):
      result+= [i *2]
    return result     

my_lst= [1,2,3,4]
print doubles2 (my_lst)
 
