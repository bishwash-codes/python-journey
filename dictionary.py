#nested dictionary
student = {
    'subject' : {
        'physics': 98,
        'chemistry': 91,
        'maths': 95
    },
    'name' : 'christy',
}

student.update({'roll no.' : 7})
print(student)

      