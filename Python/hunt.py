##                                                   DEMBA SISSOKO


## This program is designed to predict the likelyhood of someone getting Huntington disease based on the CAG count
## in their dna sequence.  It uses three function to achieve that task.  The program get the dna seqeunce, count the CGA
## repeats, and generation a prediction. This is achieve by using three functions: get_input, countCAG, and prediction.

def get_input():
    """
      The first function, get_input will prompt the
      user to provide the user to provide first name, last name, and dna sequence.  Those inputs are respectively stored
      in global variables "fname", "lname", "DNA".  The value of global variable DNA, the dna sequence provided by the user, is
      then  passed on to the function  countCAG to be counted.The values of fname, lname and DNA will be printed in the main program once
      the user input the required information at the prompt from get_input function.
    """
    
    first_name =  raw_input("Please provide your first name ")
    
    last_name  =  raw_input("Please provide your last name ")
    
    dna        =  raw_input("Please provide your DNA sequence ")
    
    return  first_name, last_name, dna


def countCAG(DNA):
    """  This function is set to receive and count the dna sequence provided by the user through the get_input()function. It will count
         the contiguous succession of the CAG string. It will terminate the count once it has reached the end of the sequence or the when
         the contiguous sequence of CAG has been interrupted by a string that is not a CAG. When the function stops counting the CAG string the ,
         the result is passed on to the function prediction() through the global variable "numCAG". Global variable "numCAG" will be printed in the
         main program. For this function to work as designed, the dna sequence provided by the usermust begin with a CAG string. If that
         condition is not met, it will not start a count. 
         
    Examples:
    >>> countCAG("C")
    0
    >>> countCAG("CAGCA")
    1
    >>> countCAG("CAGCATCAGCAGCAG")
    1
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA")
    41
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCATCACGACCAG")
    7
    >>> countCAG("CAGCAGCAGGACCAG")
    3
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGACAGCATCACGACCAGCAGCAGCAG")
    12
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAG")
    43
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAG")
    12
    """
     
    start = 0
    stop  = 3
    count = 0
    while start< len(DNA):
          if DNA[start:stop] == "CAG":
             count+= 1
             start+= 3
             stop+=  3
          else:
             return count
    return count


def prediction(numCAG):
    """
         After receiving the CAG count from the global variable numCAG, this function output the classification and disease status of the user based
         on the CAG count received from countCAG via the global variables "classification" and "stat" respectively outputting the user classification
         and disease status. Both global variables "classification" and "stat" will be printed in the main program.
         
    Examples:
    >>> prediction(27)
    ('Normal', 'Unaffected')
    >>> prediction(35)
    ('Intermediate', 'Unaffected')
    >>> prediction(42)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(45)
    ('Full Penetrance', 'Affected')
    >>> prediction(28)
    ('Intermediate', 'Unaffected')
    >>> prediction(37)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(36)
    ('Intermediate', 'Unaffected')
    >>> prediction(4)
    ('Normal', 'Unaffected')
    """
    if numCAG < 28:
        return ('Normal', 'Unaffected')

    elif 28 <= numCAG <= 36:
        return ('Intermediate', 'Unaffected')
                
    elif 37 <= numCAG <= 42:
        return ('Reduced Penetrance', 'Somewhat Affected')
        
    else:
        return ('Full Penetrance', 'Affected')
    
  
fname,lname, DNA = get_input()
numCAG = countCAG(DNA)
classification, stat = prediction(numCAG) 

print "Hello", fname, lname
print "The dna string your provided is", DNA
print "Your CAG count is ", numCAG
print "Your classification is", classification
print "Your disease status is", stat



if __name__ == '__main__':
    import doctest
    doctest.testmod()
          
