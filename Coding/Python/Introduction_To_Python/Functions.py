'''
Functions - a block of organized , reusable code to perform a particular action.
Types of functions :
1. Built-in Function - print() , input() etc.
2. User-defined Functions 
'''

#Function to calculate the factorial , with required parameter.
def factorial(n): #Function definition with parameter
    fact = 1

    for i in range(1,n+1):
        fact *= i
    return fact  #return statement

print(factorial(5)) #Calling a function with arguments

#Function with Default Arguments
def func(name , age = 35):
    print("Name:",name)
    print("Age:",age)

func("Ashwini" , 63)
func("Prachi")

#Functions with Keyword arguments
def func1(name , age = 23 , city = "Delhi"):
    print("Name:",name)
    print("Age:",age)
    print("City:",city)

func1("Ashwini" , 26)
func1("Prachi")
func1("Rahul" , city = "Bengaluru")

#Function with Variable length parameters
def func2(*args):
    print("Variable Length keyword functions:",args)

func2(1,2,3,4,5,67,8)
