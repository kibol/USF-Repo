##2
def count_letters (string, letter):
    
   count= 0 
   for char in string:
      if char == letter:
         count+= 1
   return count

print count_letters ("banana","a")

print count_letters ("martini","i")
         
print count_letters ("Mississippi","s")

print count_letters ("Missiiiiiiiiiiissippiiiiiiiiiii","i")
