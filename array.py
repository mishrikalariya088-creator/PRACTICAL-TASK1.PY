#1:integer array
from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

#1 len() array of elements
from array import array
arr=array ('i',[10,20,30,40,50])
print(len(arr))

#2 append(x)-add element at end
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#3 insert (pos,x)-insert at position
arr=array('i',[10,20,40])
arr,insert(2,30)
print (arr)

#4 remove(x)-remove first occurrence
aee=array('i',[10,20,30,20,40])
aree.remove(20)
print(arr)

#5 pop()-remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#6 index(x)-find index of elements
arr=array('i',[10,20,30,40])
print(arr.index(30))

#7 count (x)-count occurrences
arr=array('i',[10,20,30,20,40])
print(arr-count(20))

#8 reverse()-reverse array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)