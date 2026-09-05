with open("practise.txt", "w") as f:
    f.write("hey\n")
    f.write("learning about files\n")
    f.write("going well")


with open("practise.txt", "r") as f:

    data = f.read()

new_data = data.replace("hey", "HI")
print(new_data)

with open("practise.txt", "w") as f:
    f.write(new_data)
