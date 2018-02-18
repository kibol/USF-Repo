def most_occur(s):
    most_sub= ""
    s2= 1
    i= 0
    while i < len(s): 
        if s[i]== s2:
           most_sub = s[i]
           i+= 1
    return most_sub
     
print most_occur("banana")    
    
