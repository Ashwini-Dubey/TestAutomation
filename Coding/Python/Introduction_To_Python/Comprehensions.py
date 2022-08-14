'''
Comprehensions are syntactic constructs that enable sequences to be built from other sequences in a clear and
concise manner.
Types of Comprehensions :
1. List Comprehensions
2. Set Comprehensions
3. Dictionary Comprehensions
'''

#List Comprehensions
listComp = ["Auto","Honda","Benz","Tesla","Suzuki","Volkswagen","Morris Garages"]

#Creating a list to store the length of each element from the list listComp
listComprehension = [ len(i) for i in listComp ]
print("List Comprehension: " ,listComprehension)

for i,j in zip(listComp,listComprehension):
    print( i,"-",j)


#Dictionary Comprehension
dictComp = ["Auto","Honda","Benz","Tesla","Suzuki","Volkswagen","Morris Garages"]

#Creating a dictionary to store the element and length from the list.
dictComprehension = { i : len(i) for i in dictComp}
print("Dictionary Comprehension: ",dictComprehension)

#Set Comprehension
setComp = str(input("Enter a word:\n").lower())
setComprehension = {i for i in setComp if i not in "aeiou"}
print("Set Comprehension:",setComprehension)