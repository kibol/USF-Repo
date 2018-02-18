##4
import mymodule1
import mymodule2

print (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)

##5
print "My name is %s" % __name__

##After running namespace_test.py
##My name is mymodule1
##My name is mymodule2
##False
##My name is __main__
##>>> 
## The modules that are imported have the string "My name is" added to the module
##name. The receiving module is referred to as main.

##10

##>>> s = "If we took the bones out, it wouldn't be crunchy, would it?"
##>>> s.split()
##['If', 'we', 'took', 'the', 'bones', 'out,', 'it', "wouldn't", 'be', 'crunchy,', 'would', 'it?']
##>>> type(s.split())
##<type 'list'>
##>>> s.split('o')
##['If we t', '', 'k the b', 'nes ', 'ut, it w', "uldn't be crunchy, w", 'uld it?']
##>>> s.split('i')
##['If we took the bones out, ', "t wouldn't be crunchy, would ", 't?']
##>>> 'o'.join(s.split('o'))
##"If we took the bones out, it wouldn't be crunchy, would it?"
##>>> 

##13

##infile = open('alice_in_wonderland.txt', 'r')+== open the text file
##text = infile.read()=== read the file and attach it to a variable
##infile.close()== close the file that wes read from.

##type(text) will return a string.

## 128 * [0] will a list of 128 '0'

## counts is assigned to 128 * [0] because is the ASCII system has 128
##charcaters and each character is assigned a position on the list.
## so the count will change for each character in their respective
## postion.

##for letter in text:
##    counts[ord(letter)] += 1
## Will count each characters in the text file and return its respective
## count.

## the purpose of the display function is to display each character through the loop

##outfile = open('alice_counts.dat', 'w') == open the file to write
##outfile.write("%-12s%s\n" % ("Character", "Count")) return characters and  their count
##outfile.write("=================\n")

##
##for i in range(len(counts)):
##    if counts[i]:
##        outfile.write("%-12s%d\n" % (display(i), counts[i]

## The purpose is this funciton is to display each characters of a string 
## as well the count.

## The purpose of counts[i]is return the count for character in the string.




if __name__ == '__main__':
    import doctest
    doctest.testmod()




