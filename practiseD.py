#store the data in python dictionary 

word = {
'table': [  'a piece of furniture','list of facts and figure'],
    
    "cat": "a small animal"
 }
print(word)


# wap to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary and add one by one.
# use subject as key and marks as value

info = {}

phy= int(input("enter marks of physics ;"))
chem = int(input("enter marks of chemistry ;"))
maths = int(input("enter marks of maths ;"))

info.update({'physics': phy})
info.update({'chemistry': chem })
info.update({'mathematics' : maths})

print(info)
