#For Loop - to iterate over a list of integers

listIterate = [1,2,3,4,5,6,7,8]
for i in listIterate:
    print("Iterating over a list:" ,i)

#For loop - to iterate over a string
stringIterate = "Ashwini Kumar Dubey"
for ch in stringIterate:
    print("Iterating over a string:",ch)

#For loop - to iterate over a dictionary
dictIterate = {1:['AD',22] , 2:['AK',21] , 3:['RK','23']}
for key,val in dictIterate.items():
    print("Iterating over a dictionary:",key,val)

#For loop - to iterate over keys of a dictionary
for key in dictIterate.keys():
    print("Iterating over keys in a dictionary:",key)

#For loop - to iterate over a range of values.
for r in range(1,10):
    print("Iterating over a range of values:",r)

#For loop - to iterate over a range of values in reverse order.
for r in range(100,1,-20):
    print("Iterating over a range of values in reverse order:",r)

#For loop - to iterate over a range of values with step count of 5.
for r in range(0,101,30):
    print("Iterating over a range of values with step count:",r)

#For loop - to print prime numbers 1 to 100.
