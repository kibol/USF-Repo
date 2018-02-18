##                                                              DEMBA SISSOKO

## This program is designed to predict the likelihood of someone getting Huntington disease based on the CAG count
## in their dna sequence.  It uses three functions to achieve that task.  The program gets the dna seqeunce, count the CAG (codon for Huntington)
## repeats, and generates a prediction based on the number of CAG. This is achieved using these functions: get_input(), countCAG(), and prediction().

def get_input():
    """
      This function get_input will prompt the user to provide first name, last name, and dna sequence which are returned when get_input is invoked
      
    """
    
    first_name =  raw_input("Please provide your first name ")
    
    last_name  =  raw_input("Please provide your last name ")
    
    dna        =  raw_input("Please provide your DNA sequence ")
    
    return  first_name, last_name, dna


def countCAG(DNA):
    
    """
    countCAG is set to receive and count the number of CAG repeats in the dna sequence provided by the user. It will return the CAG count
    For a count to be returned two preconditions have to be met: the dna sequence provided by the user must begin with a CAG string
    (otherwise count will be 0); the succession of the CAG string must be contiguous(counting will stop if a non-CAG is found in the process.) 
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
         This function receives the count of CAG and returned a disease status and classification.  
         
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
    >>> prediction(43)
    ('Full Penetrance', 'Affected')
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
          
