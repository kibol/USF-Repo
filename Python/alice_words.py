from wordtools import*

infile = open("alice_in_wonderland.txt",'r')
word_counts = {}
while True:
    line = infile.readline()
    if line == '':
        break
    if "--" in line:
      line = line.replace('--',' ')
    line = line.split()
    for words in line:
      if words == "":
         pass
      else:  
        cleaned_word = cleanword(words)
        cleaned_word = cleaned_word.lower()
        word_counts[cleaned_word] = word_counts.get(cleaned_word,0)+ 1
word_counts = word_counts.items()
word_counts.sort()
word_counts[1:]   
outfile = open('word_counts.dat', 'w')
outfile.write("%-20s%s\n" % ("Word", "Count"))
outfile.write("=================\n")
for tup in word_counts:
      outfile.write(" %-20s%s\n" % (tup[0],tup[1]))


infile.close()
outfile.close()

  
  


