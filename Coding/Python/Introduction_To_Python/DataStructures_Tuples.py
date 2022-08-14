'''
Data Structure is a collection of data values.. 
There are multiple data sctructures because each data structure has its unique properties.
There are 4 types of data structures in Python viz. Lists , Tuples , Sets & Dictionaries.

Tuples - Contains a ordered-sequence of comma-separated values within parenthesis.Tuples are immutable, wich means
elements of a tuple can't be altered.Tuples allow duplicate values.
'''
#Sample Tuple
tupleSample = ("Ashwini" , 26 , "QA" , "98021")
print("Tuple:" , tupleSample)

#Data type of data structure
print("Data Structure Type:" , type(tupleSample))

#Tuple without the parentheses
tupleSample1= "Rahul" , 6 , "BA" , True
print("Tuple without Parentheses:" , tupleSample1)

#Data type of data structure
print("Data Structure Type:" , type(tupleSample1))

#Single-value Tuple
tupleSample2= 1,
print("Single-valueTuple without Parentheses:",tupleSample2)

tupleSample3= (99,)
print("Single-value Tuple:", tupleSample3)

#Indexing in Tuples
print("Value of element at index 0 of tupleSample:" , tupleSample[0])
print("Value of element at index 1 of tupleSample:" , tupleSample[1])
print("Value of element at index 2 of tupleSample:" , tupleSample[2])
print("Value of element at index 3 of tupleSample:" , tupleSample[3])

#Negative Indexing
print("Value of element at reverse index 1 of tupleSample:" , tupleSample[-1])
print("Value of element at reverse index 2 of tupleSample:" , tupleSample[-2])
print("Value of element at reverse index 3 of tupleSample:" , tupleSample[-3])
print("Value of element at reverse index 4 of tupleSample:" , tupleSample[-4])

#Slicing in Tuples
print("Slicing in tuples:" , tupleSample[1:])
print("Slicing in tuples:" , tupleSample[0:2])
print("Slicing in tuples:" , tupleSample[:-1])

#Concatenation of Tuples
tupleSample4 = tupleSample + tupleSample1 + tupleSample2 + tupleSample3
print("Concatenated Tuples:",tupleSample4)

tupleLength = (1,2,3,4,5,6,8,9,100)

#Sum of elements in a tuple
print("Sum of elements in tuple:",sum(tupleLength))

#Min. value in a tuple
print("Minimum value of an element in tuple:",min(tupleLength))

#Max. value in a tuple
print("Maximum value of an element in tuple:", max(tupleLength))

#Length of a tuple
print("Length of a tuple:",len(tupleLength))

#Checking the immutability of a tuple
#tupleLength[3] = 98
#print(tupleLength)

#Adding a value to the tuple
new_tuple = tupleLength[0:3] + ("Ashwini",) + tupleLength[4:]
print("New Tuple after adding an element:",new_tuple)

#Sorting a tuple
print("Sorted Tuple:",sorted(tupleLength))

#Nested Tuple
tupleNested = (1,2,3,45,85,("Ashwini" , "QA"),"Prachi")
print("Nested Tuple:",tupleNested)
print("Specific element in a nested tuple:",tupleNested[5][0])