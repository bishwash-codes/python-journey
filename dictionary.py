#nested dictionary
student = {
    'name' : 'christy',
    'subject' : {
        'physics': 98,
        'chemistry': 91,
        'maths': 95
    }
}

student.update({'roll no.' : 7})
print(student)

      