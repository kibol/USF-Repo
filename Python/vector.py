class Vector:
    
    def __init__(self, numlist):
        self.numlist = numlist     
        
    def __str__(self):
        return  str(self.numlist)
    

    def __len__(self):
        return  len(self.numlist)


    def __getitem__(self, idx):
        """ allows for indexing in accessing an element. Example:
        >>> v1 = Vector([1,2,3,4])
        >>> v1[0]
        1
        """
        return self.numlist[idx]

 
    def __setitem__(self, idx, item):
        """ allows for indexing in asigning na element. Example:
        >>> v1 = Vector([1,2,3,4])
        >>> v1[0] = 100
        >>> print v1
        [100, 2, 3, 4]
        """
        self.numlist[idx] = item


    def __mul__(self, other):
      
      result= 0
      for i in range (len(self.numlist)):
        prod = self.numlist[i]*other.numlist[i]
        result += prod
      return result

    def __add__(self, other):

      result= []
      for i in range (len(self.numlist)):
        sum_list= [self.numlist[i]+other.numlist[i]]
        result+= sum_list
      return Vector(result)


    def __rmul__(self, other):

     result =[]
     for elem in self.numlist:
        new_list=[elem*other]
        result= result+ new_list
     return Vector(result)
        

if __name__ == '__main__':  

    mynumlist = [2,1,3,5,6,7]
    v1 = Vector(mynumlist)
    print v1
    print len(v1)
    print v1[3]
    v1[1]= 4
    print v1
    v2= Vector([2,1,4])
    v3= Vector([1,3,2])
    num= v2*v3
    v5= v2+v3
    print num
    print v5
    test1= v5*v3
    print test1
    print num*v5 




