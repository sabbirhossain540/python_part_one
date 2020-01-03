
def my_func(param1 = 'Default'):
    """
        THIS IS THE DOC STRING. IT SUGGEST WHEN WE WRITE FUNCTION IT SUGGEST US
    """
    print("My First Function in Python. {}".format(param1))

my_func()


def addNum(num1, num2):
    if type(num1) == type(num2)==type(10):
        return num1 + num2
    else:
        return "Sorry Invalid Input"

print(addNum(85,"42"))




#Filter

myList = [5,8,6,2,1,4,2,5,1,6,2,3]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,myList)
print(list(evens))

#lamda Expression

list1 = [5,6,2,4,5,1,6,2,5,4,7]
even1 = filter(lambda nums:nums%2 == 0, list1)
print(list(even1))

print('x' in [1,2,3,'x'])
