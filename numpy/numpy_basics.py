import numpy as np

array_1 = np.array(
    [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]]
)
print(array_1 * 2)
print(array_1.ndim)
print(array_1.shape)
print(array_1[0][0][0])  # chain indexing
print(array_1[0, 0, 0])  # multi dimensional indexing

sum = array_1[0, 3, 1] + array_1[0, 2, 1] + array_1[0, 1, 0]
print(sum)
