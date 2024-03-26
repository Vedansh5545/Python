import numpy as np 

array = np.array([1,2,3,4])
print("Declred array A")
print(array)
print()

array2 = np.array([5,6,7,8])
print("Declred array B")
print(array2)
print()


print("Array + 2")

print(array + 2)

print()

print("Array - 2")

print(array - 2)

print()

print("Array * 2")

print(array * 2)

print()

print("Array / 2")

print(array / 2)

print()

print("Array A + Array B")

print(array + array2)

print()

print("Array A ^ 2")

print(array ** 2)

print()

################################################################

#                Trigonometry

################################################################ 


print("################################################################")
print("                         Trigonometry")
print("################################################################")
print()

# sin cos tan

a = np.array([0,30,45,60,90])

print("Array:")

print(a)

print()

print("Sin")

print(np.sin(a))

print()

print("Cos")

print(np.cos(a))

print()

print("Tan")

print(np.tan(a))

print()


################################################################

#                Linear Algebra

################################################################ 


print("################################################################")
print("                         Linear Algebra")
print("################################################################")
print()

# Create a 2x3 matrix filled with 1s
a = np.full((2,3), 1)
print("Matrix A:")
print(a)
print()

# Create a 3x2 matrix filled with 2s
b = np.full((3,2), 2)
print("Matrix B:")
print(b)
print()

  # Perform matrix multiplication between A and B
c = np.matmul(a,b)
print("Matrix C (A * B):")
print(c)
print()

################################################################

#                Statitics

################################################################ 


print("################################################################")
print("                         Statistics")
print("################################################################")
print()

stats = np.array([[1,2,3],[4,5,6]])

print("Array:")

print(stats)

print()

print("Min")

print(np.min(stats))

print()

print("Max")

print(np.max(stats))

print()

print("Sum")

print(np.sum(stats))

print()

# reorganising arrays

print("Transpose")

print(np.transpose(stats))

print()

print("Mean")

print(np.mean(stats))

print()

