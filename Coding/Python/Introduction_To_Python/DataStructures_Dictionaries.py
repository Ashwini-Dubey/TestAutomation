'''
Dictionary - Stores elements as key-value pairs. Key is like an index and its always unique and immutable.
Values are the objects that contains information. Values are accessed using their keys. Each key is followed
by a value separated by a colon. Values in a dictionary can be immutable, mutable or duplicates.Each key and
value pair is separated by a comma enclosed inside curly brackets.
'''

#Creating a sample dictionary
sampleDictionary = { "Name":"Ashwini Dubey","Organization":"Signeasy","Department":"QA Team","Age" : 26}
print("Sample Dictionary:",sampleDictionary)

#Accessing the dictionary value using the key.
print("Accessing the value of a key:",sampleDictionary["Name"])

#Replace the value for a key in a dictionary
sampleDictionary["Age"] = 25
print("Dictionary after replacing the value of Age key:",sampleDictionary["Age"])

#Inserting new key value pair in a dictionary 
sampleDictionary["Salary"] = 329130
print("Dictionary after inserting Salary key-value pair:" ,sampleDictionary)

#Deleting a key value pair from a dictionary
del sampleDictionary["Organization"]
print("Dictionary after deleting Organization key:",sampleDictionary)

#Sorting a dictionary
print("Sorted Dictionary:", sorted(sampleDictionary))

#Accessing all the values in a dictionary
print("Accessing all the values in a dictionary:",sampleDictionary.values())

#Accessing all the keys in a dictionary
print("Accessing all the keys in a dictionary:",sampleDictionary.keys())

#Updating key-value pair in a dictionary
sampleDictionary.update({'Age': 24})
print("Updating a key-value pair in a dictionary:",sampleDictionary)

