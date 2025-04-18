# πλειάδες - tuples
#print(id(str))
tu = (1,2,3)
print(tu)
print(tu[:2])

li = (1, 2, 3, 4)
print (li[1:2])

li = [(1, 2), (3, 4)]
print(len(li[1]))
li.remove((3, 4))
li.pop()
#li[0].pop()    IndexError: list index out of range


tu = ([1, 2], [3, 4])

len(tu[1])
#tu.remove([3, 4])             'tuple' object has no attribute 'remove'
#tu.pop()...................................""
tu[0].pop()      #pop last of item 0=[1,2] >>2

a=[1,2,3]
b=a
c=a.copy()
a[0]=8
print(a,b,c)
#......................................JOIN
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with whatever.....
print(' '.join(text))
print(''.join(text))
print('*'.join(text))