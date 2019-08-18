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
