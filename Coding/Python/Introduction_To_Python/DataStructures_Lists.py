'''
Lists - Contains a ordered-sequence of comma-separated values within brackets. Lists are immutable which means 
elements of a list can be altered. Lists allow duplicate values.
'''

#Sample List
listSample = ["Ashwini",26,"DevOps",92130]
print("List:",listSample)

#Nested List
listNested =  [1,2,3,45,85,("Ashwini" , "QA"),"Prachi"]
print("Nested List:",listNested)

#Accessing List elements using Index.
listIndex =  [85,("Ashwini" , "QA"),"Prachi"]
print("List Indexed:",listIndex[-1])

#Slicing the list using slicing operator(:)
print("List Sliced:",listIndex[0:])

#Membership in Lists
print("Membership in Lists:","Ashwini" in listIndex)

#Concatenation in Lists
listConcat = listSample + listNested + listIndex + ["Signeasy","VVDN Tech"]
print("Concatenation of lists:",listConcat)

#Element Replacement in Lists
listIndex[-1] = "Appster"
print("List with element replacement:",listIndex)

#Extended List
listIndex.extend([10,20,20,30,20,40])
print("Extended List:",listIndex)

#Appending element to a list
listIndex.append([5,8])
print("Appended List:",listIndex)

#Deleting an element from a list at index -4
del listIndex[-4]
print("List after del :",listIndex)

#Deleting the list
listIndex.pop()
print(listIndex)

#Removing the elements from a list
listConcat.remove("VVDN Tech")
print(listConcat)

#Sorting the list
listSort = [93,28,73,29]
listSort.sort()
print("Sorted List:",listSort)

#Sorting the list in reverse order
listSort.sort(reverse=True)
print("Reversed Sorted List:",listSort)

#Sort method alters the original list while sorted method leaves the original list untouched.
sortList = ["Apple","Carrot","Strawberry","Mango"]
newSortList = sortList.sort()

print("List before sort():",sortList)
print("List after sort():",newSortList)

sortedList = ["Apple","Carrot","Strawberry","Mango"]
newSortedList = sorted(sortedList)

print("List before sorted():",sortedList)
print("List after sorted():",newSortedList)