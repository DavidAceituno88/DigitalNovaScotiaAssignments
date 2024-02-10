contacts = {'number':4,
            'students': 
                [
                    {'name':'Sarah Holderness', 'email':'sara@example.com'},
                    {'name':'Harry Potter', 'email':'harry@example.com'},
                    {'name':'Hermione Granger', 'email':'hermione@example.com'},
                    {'name':'Ron Weasley', 'email':'ron@example.com'}

                ]
            }

print('Students emails: ')
for students in contacts['students']:
    print(students['email'])
