""" Array tutorial """

from array import *

''' creating array '''
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.4, 2.5])
print(arr1)
print(arr2)


''' traversing array '''
for item in arr1:
    print(item)


''' access element in array '''
print(arr1[2]) # access element at index 2
print(arr1[0])


''' inserting value at given index in array '''
arr1.insert(5,8) # insert value 8 at index 5
print(arr1)
arr1.insert(2,0)
print(arr1)


''' append element in array '''
arr1.append(7)
print(arr1)


''' extend array using extend() method '''
temp_arr = array('i', [10,11,12])
arr1.extend(temp_arr)
print(arr1)

''' add items from list into array using fromlist() method '''
templist = [10, 11, 12]
arr1.fromlist(templist)
print(arr1)

''' remove any array element using remove() method '''
arr1.remove(11)
print(arr1)

''' remove last element using pop() method '''
arr1.pop()
print(arr1)

''' fetch index of any element using index() method '''
print(arr1.index(10))

''' reverse an array using reverse() method '''
arr1.reverse()
print(arr1)

''' get array buffer_information through buffer_info() method '''
arr_bufferInfo = arr1.buffer_info()
print(arr_bufferInfo)

''' covert an array to a python list using tolist() method '''
print(arr1.tolist())

''' slice elements from the array '''
print(arr1[1:4])