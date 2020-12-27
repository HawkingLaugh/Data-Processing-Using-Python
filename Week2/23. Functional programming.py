# map()
lst = [3,2,5,8,1]
l2 = list(map(lambda x: x*2, lst))
print(l2)

# filter()
list2 = [1,2,3,4,5,6]
flist2 = list(filter(lambda x : x%2 == 0, list2))
print(flist2)

from functools import reduce
# reduce()
list3 = []
for i in range(1,51):
    list3.append(i)
rlist3 = reduce(lambda x,y: x + y,list3)
print(rlist3)

list4 = ['12', '3.45', '678']
mlist4 = list(map(lambda x: eval(x), list4))
print(mlist4)

mlist5 = list(map(str, mlist4))
print(mlist5)

list6 = ['abc', 'def', 'ghi']
mlist6 = list(map(lambda x:x.upper(),list6))
print(mlist6)