'''
Map - a function which works like list comprehensions and for loops. Used to map or implement functions on
various elements at the same time.

Syntax:
map(function,iterableObject)
'''
#Map Functions
countries = ["India" ,"Japan" , "Italy" , "France"]

#Output of map function has to be converted to List/tuple , for the readability purpose.
print(list(map(lambda x: x.upper(),countries)))
print(tuple(map(lambda x: x.lower(),countries)))

#Map function using the object.
def multi(x):
    return x+2
list_numbers = [1,2,4,5,6,10]
map_sample = map(multi , list_numbers)
print(list(map_sample))