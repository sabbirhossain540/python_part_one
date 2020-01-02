
#Problem 1 (INDEXING)

s = 'django'
print(s[0]) # d
print(s[-1]) # o
print(s[:4]) # djan
print(s[1:4]) # jan
print(s[4:]) # go
print(s[::-1]) #ognajd

#### Problem 2 (LIST)
l = [3,7,[1,4,'hello']]
l[2][2] = 'Good Bye'
print(l[2][2])

#### Problem 3 (dICTIONARY)

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k3':[{'nest_key':['this is deep',["hello"]]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k3'][0]['nest_key'][1][0])


##### problem 4 (SET)

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]
converted = set(mylist)
print(converted)


### Problem 5 (FORMATTING)

age = 4;
name = "Sammy"
print("Hello my dog's name is {} and he is {} years old".format(name,age))
