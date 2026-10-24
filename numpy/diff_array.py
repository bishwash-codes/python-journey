import numpy as np

# zero
array_0 = np.zeros(5)
arr_0 = np.zeros((2, 3, 7))
print(array_0)
print(arr_0)

# ones
array_1 = np.ones(10)
arr_1 = np.ones((2, 3, 2))

print(array_1)
print(arr_1)

# empty
empty_arr = np.empty(5)
print(empty_arr)

# range
range_array = np.arange(9)
print(range_array)

# diagonal 1

identity_array = np.eye(4)
iden_array = np.eye(3, 6)

print(identity_array)
print(iden_array)

# linspace

array = np.linspace(1, 10, num=5)
print(array)
