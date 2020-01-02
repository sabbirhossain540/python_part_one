#mylist = [1,2,3]
#mylist = ['this is My List','1','2','3',True,"sdfsvs",[5,6,4],False]
#print(mylist)
#print(len(mylist))
#print(mylist[:3])
#print(mylist[2:5])
#print(mylist[::3])
#mylist.append("New Item")
#print(mylist)
#listTwo = ['A','B','C']
#mylist.append(listTwo)  result: ['this is My List', '1', '2', '3', True, 'sdfsvs', [5, 6, 4], False, 'New Item', ['A', 'B', 'C']]
#mylist.extend(listTwo) result:['this is My List', '1', '2', '3', True, 'sdfsvs', [5, 6, 4], False, 'New Item', 'A', 'B', 'C']
mylist = ['A','B','C','D','E']
#item = mylist.pop(1)
mylist.reverse()
print(mylist)
#print(item)
mylist2 = [1,2,5,3,6,2,3]
mylist2.sort()
print(mylist2)

#LIST COMPRIHENSON
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
