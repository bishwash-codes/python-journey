import numpy as np

marks = np.array(
    [
        [78, 65, 82],
        [45, 38, 50],
        [90, 88, np.nan],
        [55, 72, 61],
        [30, 42, 35],
        [67, 59, 74],
        [88, 91, 85],
        [49, 51, 44],
    ]
)


def avg_student(x):
    average = np.nanmean(x, axis=1)
    return average


# or without ignoring missing val(not efficient)
# sum_s = np.sum(marks, axis=1)
# return sum_s / marks.shape[1]


def avg_sub(x):
    average_s = np.nanmean(x, axis=0)
    return average_s


#    or without ignoring missing val (not effficent)
# sum = np.sum(marks, axis=0)
# average_s = sum / marks.shape[0]
# return average_s

print(avg_student(marks))
print()
print(avg_sub(marks))
print()

student_avg = avg_student(marks)
result = np.where(student_avg >= 40, "pass", "fail")
print(result)

topper = np.argmax(avg_student(marks))
print(topper)

first_sub = marks[:, 0:1]
first_sub_highscore_index = np.max(first_sub)
print(first_sub[first_sub > 80])
