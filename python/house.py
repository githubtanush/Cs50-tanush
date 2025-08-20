name=input("what's your name? ")
'''if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")'''


'''if name == "Harry" or name == "Hermione" or  name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")'''

# match is used like the same idea as if elif or else matching is the
# same idea just like if else elif it is new use keyword in python
match name: 
    case "Harry" | "Hermione" | "Ron": #case - it is a keyword which is used with word match 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # _ means when any case has not been yet handled then print this
        print("Who?")