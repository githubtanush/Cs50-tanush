#Ask user for their name
name = input("What's your name? ")# space before the double quote to become more readable
name = name.strip()#this is used when we written inside with space in terminal but it should not include the space
name = name.capitalize()# capitalize is used for capital the just only first letter of word
name = name.title()#title is used to capitalize the all words first letter
print(f"Hello, {name}")
#Say hello to user
print("Hello, ", end="???")#end is used that at the end of the line which will create
print(name)
print("Hello,", name, sep='$$')# sep is used that at the mid of the line which will used to seperate
print("Hello, " + name)# add do not create space but it concatinate things means adding things
print("Hello, ", name)# comma create automatically one space more
print("Hello, \"friend\"")
print(f"Hello, {name}")#f= format string in python and f say that it is clue that it is format string

# for small the code write like this
#name = input("What's your name? ").strip().title()

