import numpy as np

marks = np.array([[55, 42, 71, 34, 55], [33, 52, 98, 21, 81]])


excellent = marks[marks > 90]
print("excellent ;", excellent)
print()
very_good = marks[(marks > 80) & (marks <= 90)]
print("very good :", very_good)
print()
good = marks[(marks > 70) & (marks <= 80)]
print("good :", good)
print()
average = marks[(marks > 50) & (marks <= 70)]
print("average :", average)
print()
fail = marks[(marks <= 50)]
print("failed :", fail)
print()
# filtering without disrupting the og structure, Example:
failed = np.where(marks > 50, marks, "fail")
print(failed)
