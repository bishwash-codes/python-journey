guests = [
    ("ritu", 33),
    ("milan", 22),
    ("rijan", 18),
    ("niranjan", 21),
    ("sharmila", 36),
    ("akriti", 17),
]
banned = [("niranjan"), ("rajan")]

allowed = []
not_allowed = []

for name, age in guests:
    if name in banned:
        not_allowed.append(name)
        print(f" {name} is banned.")
    elif age <= 18:
        not_allowed.append(name)
        print(f"{name} is only {age} so is not eligible to enter.")
    else:
        allowed.append(name)

print("Allowed to enter:  ", allowed)
print("Not allowed to enter:  ", not_allowed)
