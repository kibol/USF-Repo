class Fraction:
    def __init__(self, num, denom):
        try:
          num/denom
          self.num = num
          self.denom = denom
        except ZeroDivisionError:
          print " Cannot divide by zero"
        
    def __str__(self):
        return  str(self.num) + '/' + str(self.denom)  
    
   
    def __mul__(self, other):
       top_num = self.num * other.num 
       bottom_num = self.denom* other.denom
       return Fraction (top_num, bottom_num)

    def mult(self, other):
       top_num = self.num * other.num 
       bottom_num = self.denom* other.denom
       return Fraction (top_num, bottom_num)
       
if __name__ == '__main__':            
    test1 = Fraction(3,5)
    test2 = Fraction(4,3)
    test3 = test1.mult(test2)
    test4 = test1*test2
    final_test = test3*test4
    print final_test
    test_zero= Fraction(5,0)

    
