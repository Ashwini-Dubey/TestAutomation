#Creating a class rectangle with two attributes viz. length & breadth.
class rectangle: #Class
    def __init__(self): # Non-prameterized Constructor of class rectangle
        self.length = 10 #length is the instance variable.
        self.breadth = 15 #breadth is the instance variable

#Create the object of the class rectangle
rect = rectangle()

#Accessing the instance variable length & breadth using the object with dot operator.
print("Area :" , rect.length * rect.breadth)

print("------------------------------------------------------------------------------------")

#Creating a class square with parameterized constructor
class square:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

#Create the object of the class square
sq = square(10,20)
print("Area of the square:",sq.length*sq.breadth)
