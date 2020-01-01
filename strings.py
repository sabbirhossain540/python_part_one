#STRINGS
mystring = "Hello World"
print(mystring)

#Indexing
print(mystring[0])
print(mystring[-1])

#Slicing
print(mystring[:3])
print(mystring[3:5])
print(mystring[::2])

#Basic Method
print(mystring.upper())
print(mystring.lower())
print(mystring.capitalize())
x = mystring.split('o')
print(x)

#Print Formatting
#x = "Insert Another String Here: {}".format("INSERT ME")
#x = "Item one: {} , Item two: {}".format("Apple", "Orange")
x = "Item one: {a} , Item two: {b}".format(a = "Apple", b = "Orange")
print(x)
