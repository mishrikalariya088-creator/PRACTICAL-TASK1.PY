#basic slices
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])

#slicing whith step
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#negative slicing
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:1])
print(arr[:-2])

#reverse array using slicing
arr=array('i',[10,20,30,40,50])
print(arr[::-1])

#modifing slicps
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)

#indexing in array
#positive indexing
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#negative indexing
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])

#modifying element using index
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

