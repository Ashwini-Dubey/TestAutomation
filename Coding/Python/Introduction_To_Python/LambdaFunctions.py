'''
Lambda Functions - Way of defining functions which can take multiple parameters as input but can only execute
a single expression, in other words , they can only perform a single operation.

Syntax :
funtionName = lambda input_param : output param with expressions
'''
 
#Lambda function to check a number is odd or even.
lambdaFunc = lambda a: "even" if a % 2 == 0 else "odd"
print(lambdaFunc(10))

#Lambda function to add two numbers.
lambdaAddFunc = lambda a,b: a + b
print(lambdaAddFunc(10,209))
