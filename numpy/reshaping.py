import numpy as np

val = np.array([1, 2, 3, 4, 5])
val_re = np.array(val, ndmin=6)
print()
print(val_re)
print()
print(val_re.ndim)

value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(value.reshape(2, 2, 3))
