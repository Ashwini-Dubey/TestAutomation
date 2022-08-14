#Sample Code for Methods and functions
# #Methods are defined in a class , while functions are independent of the class.

#Creating a class rectangle
class rectangle:
    pi = 3.14
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    #Instance Method
    def calculateArea(self):
        return self.length * self.breadth

    #Class Method
    @classmethod
    def access_pi(cls):
        cls.pi = 3.1436
        return cls.pi
    
    #Static Method
    @staticmethod
    def rect_static_method():
        print("This is a static method.")


#Instantiating an objects of class rectangle
rect = rectangle(18,19)

print("Length of rectangle:",rect.length , "\nBreadth of rectangle:",rect.breadth,"\nArea of rectangle:",rect.calculateArea())

cir = rectangle(10,20)