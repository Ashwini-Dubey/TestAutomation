'''
Sets - type of collection like lists and tuples for storing mixed data. Sets are enclosed within curly brackets
and elements are written as comma-separated. Sets are unordered and doesn't allow duplicate values.
'''

#Sample Set
setSample = {1,2,3,4,5,6,7,1,3,4,5,5}
print("Sample Set:",setSample)

#Length of a set
print("Set Length:",setSample)

#Adding an element to the set.
print("Set before adding an element:",setSample)
setSample.add('India')
print("Set after adding an element:",setSample)

#Set Operations
A = {1,2,3,4,5,6,7,8,9,0}
B = {9,1,3,3,14,94,29,21}

#Union of sets
print("Union of sets A & B:" , A | B)
print("Union of sets A & B:" , A.union(B))

#Intersection of sets
print("Intersection of sets A & B:", A & B)
print("Intersection of sets A & B:", A.intersection(B))

#Difference of sets
print("Difference of sets A & B:", A - B)
print("Difference of sets A & B:", A.difference(B))

#Symmetric Difference of sets
print("Symmetric Difference of sets A & B:", A ^ B)