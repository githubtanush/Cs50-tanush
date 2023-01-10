#students = ["hermione","Harry","Ron"]
#for s in students:
#    print(s)
'''for s in range(len(students)):       # range= range is used to define the range of function so that we don't write more
         # len = list is used to list all the values
                # dict= dictionary  is used to arrange somethings in order used curly brackets for dict
    print(s+1, students[s])'''


# use of dict
students= {"Hermione":"Gryffindor",
"Harry":"Gryffindor",
"Ron":"Gryffindor",
"Draco":"Slytherin",
}
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])
for student in students:
    print(student, students[student],sep=",")
