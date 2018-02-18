##12

source_text = open('unsorted_fruits.txt', 'r')
fruits = source_text.readlines()
source_text.close()
fruits.sort()
newfile = open('sorted_fruits.txt', 'w')
newfile.writelines(fruits)
newfile.close() 
