def get_input():
    n = input (" Please enter a positive integer of at least 2 digits\n")
    return n 

def reverse_digits(n):
    
    reverse = 0 
    while n:
        last_num = n%10
        reverse = (reverse*10)+last_num
        n = n/10
    return reverse

userent = get_input()

reversal = reverse_digits (userent)

print " Your entry", userent, " was reversed to ", reversal




