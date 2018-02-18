##2

def count_letters(word, substr):
    
    count = 0
    for char in word:
       if char == substr:
         count += 1        
    return count

print count_letters ("banana", "a")
 

