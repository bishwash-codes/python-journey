import numpy as np

nums = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

print(np.argmin(nums))
print(np.sum(nums))

print(np.sum(nums, axis=0))  # axis= 0 le coloumn sum
print(np.sum(nums, axis=1))  # row sum

print(np.mean(nums))
print(np.median(nums))
print(np.var(nums))
print(np.std(nums))
