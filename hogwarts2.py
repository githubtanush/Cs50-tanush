students=[
    {"name": "hermione","house":"Gryffindor","patronus":"Otter"},
     {"name": "harry","house":"Gryffindor","patronus":"Stag"},
    {"name": "Ron","house":"Gryffindor","patronus":"Jack Russel terrier"},
    {"name": "Draco","house":"Slytherin","patronus":"None"},
]

for student in students:
    print (student["name"], student["house"],student["patronus"],sep=", ")
#None - in python it is literally none included