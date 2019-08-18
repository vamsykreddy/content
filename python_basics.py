class Fun:
  pass
f = Fun()
print(f) #prints object instance and it's memory location

class Fun:
  def __str__():
    s = "This is an object instance"
    return s
f = Fun()
print(f) #This is an object instance is printed

# __str__() method is invoked whenever print (or __str__()) is called
# __add__() method is invoked whenever + operator is used with an object

######################## FUN below 

import math

class Point:
    def __init__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__ (self):
        s = f'Point: ({self.x} {self.y} {self.z})'
        return s
    def distance(self,other):
        distance = math.sqrt( (self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
        return distance
    def __add__(self,other):
        new_x = self.x+other.x
        new_y = self.y+other.y
        new_z = self.z+other.z
        return Point(new_x,new_y,new_z)
        
p1 = Point(4, 5, 6)
p2 = Point(-2, -1, 4)
print(p1.distance(p2))
print(p1+p2)
