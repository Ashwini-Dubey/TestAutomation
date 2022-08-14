#Sample Code for Class Variables and Instance Variables.

#Creating a class circle
class circle:
    pi = 3.14 #Class Variable pi
    
    def __init__(self,radius): #Parameterized Constructor
        self.radius = radius #Instance Variable radius

#Create object of class circle
circle_1 = circle(10)
print("Radius of the circle:" , circle_1.radius)
print("Pi of the circle:" , circle_1.pi)

circle_2 = circle(2)
print("Radius of the circle:" , circle_2.radius)
print("Pi of the circle:" , circle_2.pi)


#Accessing the class variable outside the class
circle.pi = 3.1436

#Create object of class circle
circle_3 = circle(10)
print("Radius of the circle:" , circle_1.radius)
print("Pi of the circle:" , circle_1.pi)

circle_4 = circle(2)
print("Radius of the circle:" , circle_2.radius)
print("Pi of the circle:" , circle_2.pi)