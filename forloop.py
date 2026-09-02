# to find the value in a gvn tuple


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter a no. to search "))
i = 0
for val in num:
    if val == x:
        print(val, "found at index", i)
        break
    i += 1
else:
    (print("not found"))

print("end")
