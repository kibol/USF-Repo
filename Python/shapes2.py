class Point:
   def _init_(self,x=0.0,y=0.0):
       self.x = x
       self.y = y

   def _str_(self):
       return "("+ str(self.x) + "," + str(self.y) + ")"

class Line:
##      def _init_(self,x1=0.0,y1=0.0,x2=0.0,y2=0.0):
      def _init_(self,pt1,pt2):
          self.pt1 = pt1
          self.pt2 = pt2

      def _str_(self):
          return str(self.pt1) + ":" + str(self.pt2)
          

    
ptA = Point(2,1)
print(ptA)

ptB = Point()
print(ptB)

line1 = Line(ptA, ptB)
print(line1)

line2 = Line(Point(2,1), Point())
print(line2)

print line1.pt1.x

print(line1)
print(line2)


class Fraction:
   def _init_(self,num,dem):
       
