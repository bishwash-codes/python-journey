# NumPy Stats Toolkit

Statistics functions (mean, variance, std, median, z-score) written
from scratch with NumPy, and checked against NumPy's built-in versions.
used claude ai slightly for testing of code

## What it does
- `mean`, `variance`, `std`, `median`, `zscore` in `stats_toolkit.py`
- All work column-wise on a 2D array (rows = samples, columns = features)
- Vectorized: no Python loops over rows
- Variance and std use the population formula (divide by n)

## How to run
```
pip install numpy
python test_stats.py
```
The script generates 150 fake students × 4 subjects and asserts that each
function matches its NumPy equivalent.

## Expected output
```
mean is working
variance is working
std is working
median is working
zscore is working
```

## What I learned
✍️ 
- `axis=0` makes a function work down the rows and return one result per column, so each subject is processed separately and never mixed with another.
- Broadcasting: a `(150, 4)` array minus a `(4,)` array works because shapes are matched from the right. That is how I subtracted each column's own mean without any loops.
- The median needs the data sorted first, and odd and even row counts are handled differently. My data has 150 rows (even), so I also tested on 149 rows to cover the odd case.
- Variance divides by n (population), which matches NumPy's default. Sample variance divides by n - 1, and mixing the two causes small mismatches in tests.
- I tested every function against NumPy with `np.allclose` instead of `==`, because floating-point results can differ in tiny decimals.


## Next
Linear regression from scratch (normal equation and gradient descent).