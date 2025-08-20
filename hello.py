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
print("Hello, \"friend\"")#escape characters when same type of commas is used for printing in between commas
print(f"Hello, {name}")#f= format string in python and f say that it is clue that it is format string
#or we can say that it is the special string 
# print(*objects, sep=' ',end = '\n',file = sys.stdout , flush = False)
# for small the code write like this
#name = input("What's your name? ").strip().title()

"""
 docs.python.org/3/library/functions.html -> is the main website where we read the 
 function of python 
 Learn to Read Documentation

# code hello.py - to open vs code and create file named hello.py
# sign just indicate that where u write the prompt
# computers only understand the binary numbers which is 0 and 1
# A function is like a action or verbs 
# print is also a function 
# Arguments an input to a function anything you want on the string 
# The people who invented the python would design the print function 
# with this bracket this programme ultimately doing on the screen is 
# printing the line its shown generally in the screen is generally known 
# as SIDE EFFECT

# A bug is a mistake in a programme

# could i write the code in microsoft excel ? Notepad or any restriction
# we generally want something simpler 

#if it is possible to run the programme without the terminal window?
#CLI is give us more much control on our programme
#return values 
#variables - to store the value in that memory location
# = sign copies whatever is written at the right to the left
# comments or notes to yourself by # sign

#pseudocode just the skeleton of the programme that i write this

parameters = parameters first thing you pass print first 
second thing at second 
third thing at third
"""

"""
    multiline comments
"""
