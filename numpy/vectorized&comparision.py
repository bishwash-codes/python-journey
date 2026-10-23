import numpy as np

marks = np.array([59, 50.5, 73, 81.5, 58, 100, 29, 73.5])
# vectorized math operations
print("the maximum marks is", np.amax(marks))
print("the minimum marks is", np.amin(marks))
print(np.round(marks))
print(np.sqrt(marks))
print("the value of pi is", np.pi)

# comparision operators

print(marks == 100)
print(marks >= 50.5)
marks[marks < 33] = 0
print(marks)
print(marks != 58)
