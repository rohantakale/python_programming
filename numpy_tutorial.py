# Numpy Tutorial using python 3.5.2
import numpy as np
import time
import sys

example_array = np.array((1,2,3)) 
example_array2 = np.array([(1.,2.,3.),(4.,5.,6.)])
example_array3 = np.array([(2.,3.,4.),(5.,6.,7.)])
print(example_array)
print(example_array2)


# Advantages of numpy over list
# 1. Faster 2. Less memory 3. Convenient
list1 = range(1000000)
print(sys.getsizeof(5)*len(list1))

array1 = np.arange(1000000)
print(array1.size * array1.itemsize)
# This proves that numpy takes up less memory
list2 = range(1000000)
array2 = np.arange(1000000)

start = time.time()
result = [(x,y) for x,y in zip(list1,list2)]

print((time.time()-start)*1000)

start = time.time()

result = array1 + array2
print((time.time()-start)*1000)
# This proves that numpy takes less time i.e. it is faster

# Numpy Operations
print(example_array2.ndim)		# Find dimensions of array
print(example_array.itemsize)	# Find byte size of each element
print(example_array.dtype)		# Find datatype of array elements
print(example_array2.size)		# Find size of array - totla no. of elements
print(example_array2.shape)		# Find shape of array
print(example_array2.reshape(3,2)) # Reshaping array
print(example_array2[0:,1])		# Slicing similar to matlab

array3 = np.linspace(1,3,5)
print(array3)					# Line spacing 
print(array3.max(), array3.min())	# Max and Min
print(example_array.sum())				# Find Sum
print(example_array2.sum(axis = 1))		# sum of row elements
print(example_array2.sum(axis = 0))		# sum of column elements

# square root and standard deviation
print(np.sqrt(example_array2), np.std(example_array2))	
# matrix addition, subtraction, multiplication,division
print(example_array2 + example_array3, example_array2 - example_array3, example_array2 * example_array3, example_array2 / example_array3)
# horizontal and vertical stacking
print(np.vstack((example_array2,example_array3)))
print(np.hstack((example_array2,example_array3)))
# horizontal lining up of all elements
print(example_array3.ravel())

# Numpy Special Functions
print(np.exp(example_array))
print(np.log(example_array))
print(np.log10(example_array))

print("The matrix Operations start here: ")

