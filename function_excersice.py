
#Problem 1:
#Find The Pair of 123
myList = [5,4,6,8,2,1,2,3]

def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

#print(arrayCheck(myList))

#Problem 2

def strBite(str):
    result = ""
    for i in range(len(str)):
        if(i%2 == 0):
            result = result + str[i]
    return result

#print(strBite("HelloWorld"))

#Problem 3

def endOther(a,b):
    a = a.lower()
    b = b.lower()

    return (b.endswith(a) or a.endswith(b))

#print(endOther("fddabc","abc"))

#Problem 4

def doubleChar(str):
    result = ""
    for i in range(len(str)):
        result = result + str[i]+str[i]
    return result
#print(doubleChar("Sabir"))

#Problem 5

def no_teen_sum(a,b,c):
    return no_teen(a) + no_teen(b) + no_teen(c)

def no_teen(a):
    if a in [13,15,17,19]:
        return 0
    else:
        return a

#print(no_teen_sum(5,4,13))

#Problem 6
givenList = [4,5,2,4,6,3,5,1,6]

def checkNum(nums):
    return nums%2 == 0
even = filter(checkNum,givenList)
#print(list(even))
