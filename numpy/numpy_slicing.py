import numpy

array_1 = numpy.array(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
)

# slicing
print(array_1[0 : len(array_1) : 2])  # row

print(array_1[:, 2:4])  # coloumn

print(array_1[::-1])  # reverse

# row and coloumn
print(array_1[0::2, 2:4])

print(array_1[0:2, 0:2])
