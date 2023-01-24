#exploring fancy indexing
import numpy as np
rand = np.random.RandomState(42)
x= rand.randint(100, size=10) # printing random elements till 100 only and will print 10 numbers
print(x)

# 1-D array
print([x[0], x[7], x[2]])

#2-D array
ind = np.array([[3,7],
                [4,5]])
print(x[ind])

X= np.arange(20).reshape((5,4))
print(X)
row = np.array([0,1,2])
col = np.array([2,1,3])
print(row,col)

# combined indexing
X1 = X[2,[2,0,1]]
print(X1)

# sorting arrays
x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))#  sorting the array

i = np.argsort(x) # gives the index order according to the sorted array
print(i)

# sorting along rows and columns
rand = np.random.RandomState(42)
x = rand.randint(0, 10, (4, 6))
print(x)
print(np.sort(x))
print(np.sort(x, axis=0))

print(np.sort(x, axis=1))


name = ['Alice', 'bob', 'cathy', 'doug']
age  = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

"""
# 'U10' translate the "unicode string of maximum length 10"
# 'i4'  translate the '4-byte (i.e 32 bit) integer.
#'f8'   traslates the "8-byte (i.e 64 bit) float.
"""

data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)




















