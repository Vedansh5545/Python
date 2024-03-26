'''

create a 2d array using numpy 

array -> 1 1 1 1 1
         1 0 0 0 1
         1 0 9 0 1
         1 0 0 0 1
         1 1 1 1 1

'''
import numpy as np

array = np.zeros((5,5), dtype=int)

print("initial array with all zero")
print()
print(array)

print("Changing first and last row to 1")

array[0,0] = 1

array[0:1] = 1

for i in range(5):
    array[4,i] = 1



print(array)
print()

print("Changing first and last column to 1")

array[:,0] = 1

array[:,4] = 1

print()
print(array)

print("middle element of array to 9")

array[2,2] = 9


print(array)
print()