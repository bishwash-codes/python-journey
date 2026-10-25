import numpy as np

rng = np.random.default_rng(42)
data = rng.normal(loc=[60, 70, 50, 80], scale=[10, 8, 15, 5], size=(150, 4))

print(data.shape)
print(data[:3])

print()
from stats_toolkit import mean, variance, std, median, zscore

print(mean(data))
print(np.mean(data, axis=0))
assert np.allclose(mean(data), np.mean(data, axis=0))
print("mean is working")
assert np.allclose(variance(data), np.var(data, axis=0))
print("variance is working")
assert np.allclose(std(data), np.std(data, axis=0))
print("standard deviation is working")

c = np.array([[5], [1], [3], [2], [4]])  # odd, answer [3.]
d = np.array([[4], [1], [3], [2]])  # even, answer [2.5]
print(median(c), median(d))

assert np.allclose(median(data), np.median(data, axis=0))
assert np.allclose(median(data[:149]), np.median(data[:149], axis=0))
print("median is working")

z = zscore(data)
print(mean(z))
print(std(z))
assert np.allclose(mean(z), 0)
assert np.allclose(std(z), 1)
print("zscore is working")
