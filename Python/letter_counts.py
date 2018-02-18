import string 
from sys import argv 

def mkdict():
   s = argv[1]  
   counts = {} 
   for letter in s:     
      letter = string.lower(letter)     
      if counts.has_key(letter):         
        counts[letter] = counts[letter] + 1    
      else:           
        counts[letter] = counts.get(letter, 0) + 1     
        letterList = counts.items() 
        letterList.sort() 
   for elem in letterList:     
      if elem[0] in string.ascii_letters:         
          print elem[0], elem[1]

mkdict()
