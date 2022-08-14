#While loop

i = 0
while i < 10:
    print(i)
    i += 1

#While loop with break statement
a = 1
while a < 10:
    print(a)
    if a==5:
        break
    a +=1

##While loop with continue statement
b = 0
while b < 10:
    b += 1
    if b == 5:
        continue
    print(b)

#while loop with else statement
c = 0
while c < 10:
    print(c)
    c += 1
else:
    print("c is no longer less than 10")
    