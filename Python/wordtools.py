import doctest
import string

##11

def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    new_word = ""
    for i in range(len(word)):
        if word[i].isalpha(): #or word[i]== "-": 
            new_word += word[i]
    return new_word
    
#print cleanword('-?+="word!,@$()"')


##def has_dashdash(s):
##    """
##      >>> has_dashdash('distance--but')
##      True
##      >>> has_dashdash('several')
##      False
##      >>> has_dashdash('critters')
##      False
##      >>> has_dashdash('spoke--fancy')
##      True
##      >>> has_dashdash('yo-yo')
##      False
##    """
##    for ch in s:
##        if "--" in s:
##           return True
##        else:
##           return False   



##def extract_words(s):
##    """
##      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
##      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
##      >>> extract_words('she tried to curtsey as she spoke--fancy')
##      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
##    """
##    new_list=[]
##    listed = s.split()
##    for elem in range(len(listed)): 
##        if listed[elem] .isalpha():
##            if '--' in listed[elem]:
##              listed[elem].split('--')
##        new_list += [listed[elem]]
##    return new_list
##
##print extract_words('Now is the time!  "Now", is the time? Yes, now.')
##

    
##def wordcount(word, wordlist):
##    """
##      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['now', 2]
##      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
##      ['is', 4]
##      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['time', 1]
##      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['frog', 0]
##    """
##    result= [word, wordlist.count(word)]
##    return result
##
##print wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
##    

    
##def wordset(wordlist):
##    """
##      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['is', 'now', 'time']
##      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
##      ['I', 'a', 'am', 'is']
##      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
##      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
##    """
##    new_wordlist=[]
##    for i in range (len(wordlist)):
##        if wordlist[i] in new_wordlist:
##            continue
##        else:
##           new_wordlist.append(wordlist[i]) 
##    return sorted(new_wordlist)
##
##print wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
   
##def longestword(wordset):
##    """
##      >>> longestword(['a', 'apple', 'pear', 'grape'])
##      5
##      >>> longestword(['a', 'am', 'I', 'be'])
##      2
##      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
##      34
##    """  
##    longest_word = 0
##    for word in wordset:
##      length = len(word)
##      if length > longest_word:
##         longest_word = length
##    return longest_word
##
##print longestword(['this', 'that', 'supercalifragilisticexpialidocious'])


##
if __name__ == '__main__':
    import doctest
    doctest.testmod()
