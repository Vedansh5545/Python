import numpy as np

# The Basics (creating arrays, shape, size, data type)

# Importing the module
print("Importing the module")
print()

# Declaring a 1-dimensional array
print("Declaring a 1-dimensional array")
a = np.array([1, 2, 3, 4, 5] , dtype='int16')
print(a)
print()

# Declaring a 2-dimensional array
print("Declaring a 2-dimensional array")
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print()

# Get the size of the array
print("Getting the size of the array")
print(a.shape)
print(b.shape)
print()

# Get the dimension of the array
print("Getting the dimension of the array")
print(a.ndim)
print(b.ndim)
print()

# Get the data type of the array
print("Getting the data type of the array")
print(a.dtype)
print(b.dtype)
print()

# Get item size of the array
print("Getting the item size of the array")
print(a.itemsize)
print(b.itemsize)
print()

# Get the size of the array in bytes
print("Getting the size of the array in bytes")
print(a.nbytes)
print(b.nbytes)
print()

# Get the size of the array in bits
print("Getting the size of the array in bits")
print(a.itemsize * 8)
print(b.itemsize * 8)
print()

# Get the total size of the array
print("Getting the total size of the array")
print(a.size)
print(b.size)
print()

#######################################################################
print("#######################################################################")
print()

# Accessing/Changing Specific Elements, Rows, Columns, etc (slicing)

print("Accessing/Changing Specific Elements, Rows, Columns, etc (slicing)")
print()


# Create a new array
print("Declared new array c:")
c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(c)
print()

# Get the first row

print("Get the first row")
print(c[0])
print()

# Get the specific row

print("Get the specific row")
print(c[1])
print()

# Get the first column

print("Get the first column")
print(c[:, 0])
print()

# Get the specific column

print("Get the specific column")
print(c[:, 1])
print()

# Get the specific element

print("Get the specific element")
print(c[1, 1])
print()

# Change the specific element

print("Change the specific element")
c[1, 1] = 100
print(c)
print()

# Getting a little more fancy [startindex:endindex:stepsize]

print("Getting a little more fancy [startindex:endindex:stepsize]")
print(c[1:4:2])
print()


# replace

print("replace")
c[1:4:2] = 100
print(c)
print()

#initializing different types of arrays

print("initializing different types of arrays")

#All 0s matrix
print("All 0s matrix")
d = np.zeros((2,2))
print(d)
print()

#All 1s matrix
print("All 1s matrix")
e = np.ones((2,2))
print(e)
print()

#Any other number matrix
print("Any other number")
f = np.full((2,2), 7)
print(f)
print()

#Any other number (full_like)
print("Any other number (full_like)")
g = np.full_like(c, 7)
print(g)
print()

# Random decimal numbers
print("Random decimal numbers")
h = np.random.random((2,2))
print(h)
print()

# Random integer numbers
print("Random integer numbers")
i = np.random.randint(10, size=(4,4))
print(i)
print()

# The identity matrix
print("The identity matrix")
j = np.eye(3)
print(j)
print()

# Repeat an array
print("Repeat an array")
k = np.repeat(c, 3)
print(k)
print()
