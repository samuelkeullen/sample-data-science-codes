import numpy as np
import matplotlib.pyplot as plt

#The basics and Array creation
# NORMALLY: >>>> a = ["0", 1, "two", "3", 4] #python list
#lets create a ndarray
a = np.array( [0, 1, 2, 3,  4] ) #array numpy só são feitos por itens iguais, diferente da lista python, nesse caso, integers

get_type = type(a) #get the type of the numpy array
get_dtype = a.dtype #get the dtype of the numpy array
get_size = a.size #get the lenght of the numpy array
get_ndim = a.ndim #get the dimensions of the numpy array, in this case, as a ndarray, is one dimensional
get_shape = a.shape #get the shape of the array in each dimension, separated by a tuple

m1 = "The type of the Numpy array is:\n{}\n".format(get_type)
m2 = "The dtype of the Numpy array is:\n{}\n".format(get_dtype)
m3 = "The lenght of the Numpy array is:\n{}\n".format(get_size)
m4 = "The number of dimensions of the Numpy array is:\n{}\n".format(get_ndim)
m5 = "The shape of the Numpy array is:\n{}\n".format(get_shape)

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print("")

b = np.array([ 3.1, 11.02, 6.2, 213.2, 5.2])

get_type = type(b) #get the type of the numpy array
get_dtype = b.dtype #get the dtype of the numpy array
get_size = b.size #get the lenght of the numpy array
get_ndim = b.ndim #get the dimensions of the numpy array, in this case, as a ndarray, is one dimensional
get_shape = b.shape #get the shape of the array in each dimension, separated by a tuple

m1 = "The type of the Numpy array is:\n{}\n".format(get_type)
m2 = "The dtype of the Numpy array is:\n{}\n".format(get_dtype)
m3 = "The lenght of the Numpy array is:\n{}\n".format(get_size)
m4 = "The number of dimensions of the Numpy array is:\n{}\n".format(get_ndim)
m5 = "The shape of the Numpy array is:\n{}\n".format(get_shape)

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print("")

#Indexing and Slicing
c = np.array([ 20, 1, 2, 3, 4])
print("Original value of the Numpy array C:")
print(c)
print("")

c[0] = 100
c[4] = 0

c[3:5] = 300,400

print("New value of the Numpy array C:")
print(c)
print("")

d = c[1:4] #both in the lists and the numpy arrays, we not count the last index, in this case, 4th element

print("New Numpy array by [1:4] index of C:")
print(d)
print("")


#Basic Operations
#sum of two vectors without numpy
u = [1, 0]
v = [0, 1]

z = []

for n, m in zip(u, v):
    z.append(n+m)
print("Sum of two vectors (without numpy):")
print(z)
print("")

#sum of two vectors with numpy
u = np.array([1,0])
v = np.array([0,1])

z = u + v

print("Sum of two vectors (with numpy):")
print(z)
print("")

#Array multiplication with a Scalar
y = np.array([ 1, 2 ])
z = 2 * y
print("The original Numpy Array:")
print(y)
print("")
print("Multiplication of Numpy Array with Scalar :")
print(z)
print("")

#Product of two numpy arrays:
#hadamard = u[0] * v[0] e assim por diante...
u = np.array([1,2])
v = np.array([3,2])
z = u * v

m_hadamard = "The hadamard product of this two numpy arrays: \nu = {}\nv = {}\nis equals to =\n{}".format(u, v, z)

print(m_hadamard)

#Dot product: e.g: u = [1,2] v = [3,1], uTv = 1 * 3 + 2 * 1 = 5... uTv = u[0] * v[0] + u[1] * v[1]
u = np.array([1,2])
v = np.array([3,1])

result = np.dot(u,v)

print("\nDot Product:")
print(result)
print("")

#Adding Constant to an numpy array

u = np.array([1,2,3,-1])
#if we add Scalar value to the array, numpy will add to each element
z = u+1 #in this case, for each value in u, will be added +1
print("Adding a Scalar value(+1) to each value in numpy array:")
print(z)
print("")

#Universal Functions

a = np.array([1, -1, 1, -1])
mean_a = a.mean() #to calculate the mean
print("Calculate the mean of the numpy array:")
print(mean_a)
print("")

b = np.array([1, -2, 3, 4, 5])
max_b = b.max()#get the maximum value of the array
print("Calculate the max value of the numpy array:")
print(max_b)
print("")

#to use the pi function in numpy, use:
test_pi = np.pi
print("Here, the value of PI using the numpy:")
print(test_pi)
print("")

x = np.array([ 0, np.pi / 2, np.pi])
print("The original Numpy Array:")
print(x)
print("")

y = np.sin(x)#get the in of the array
print("Sin of Numpy Array above:")
print(y)
print("")

#A useful function for plotting mathematical functions is line space
#np.linspace(a, b, c) a = the starting point, b = the ending point and c = number of samples
test = np.linspace(-2, 2, num=5)
print("New Numpy array builded with linspace with 5 samples:")
print(test)
print("")

#Plotting Mathematical Functions:

x = np.linspace(0, 2*np.pi, 100)
print("A new Numpy array builded with linspace, but with PI value * 2, with 100 samples:")
print(x)
print("")

y = np.sin(x)

print("New Numpy Array mapped from the above array, but with sin:")
print(y)
print("")
#horizontal is X and vertical is Y
#plt.plot(x,y)
#plt.show()



#2D NUMPY ARRAYS

#the baiscs and array creation in 2d
#in 2d lists, the first value in shape corresponds to the number of rows, and de second corresponds to number of columsn
a = [[11,12,13], [21,22,23], [31,32,33]]

A = np.array(a)#a rectangle array
get_type = type(A) #get the type of the numpy array
get_dtype = A.dtype #get the dtype of the numpy array
get_size = A.size #get the lenght of the numpy array
get_ndim = A.ndim #get the dimensions of the numpy array, in this case, as a ndarray, is one dimensional
get_shape = A.shape #get the shape of the array in each dimension, separated by a tuple

m1 = "The type of the Numpy array is:\n{}\n".format(get_type)
m2 = "The dtype of the Numpy array is:\n{}\n".format(get_dtype)
m3 = "The lenght of the Numpy array is:\n{}\n".format(get_size)
m4 = "The number of dimensions of the Numpy array is:\n{}\n".format(get_ndim)
m5 = "The shape of the Numpy array is:\n{}\n".format(get_shape)

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print("")

#Sum matrix
X = np.array([ [1,0], [0,1] ])
Y = np.array([ [2,1], [1,2] ])

Z = X+Y;

print("The Sum of matrices is:")
print(Z)
print("")

#Multiply matrix by 2
Y = np.array([ [2,1], [1,2] ])

Z = 2*Y;

print("The Multiply by 2 of matrices is:")
print(Z)
print("")

#hadamart for 2D matrices
X = np.array([ [1,0],[0,1] ])
Y = np.array([ [2,1],[1,2] ])
Z = X*Y;

print("The hadamard product of the matrices:")
print(Z)
print("")

#matrix multiplication
A = np.array([ [0,1,1], [1,0,1]] )
B = np.array([ [1,1], [1,1], [-1,1] ])
C = np.dot(A,B)#with the dot method, we can multiply matrices

print("The Multiply of matrices is:")
print(C)
print("")

# Indexing and Slicing in 2D

# Basic Operations in 2D

