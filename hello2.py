'''def hello():#def used to define a function in python
    print("hello")


name=input("What's your name? ")
hello()#def used to define a function in python
print(name)'''



def hello(to):#def used to define a function in python
    #to is the parameter which we use in this
    print("hello,", to)


name=input("What's your name? ")
hello(name) # to = name

def hello(to="world"):#def used to define a function in python
    #to is the parameter which we use in this
    print("hello,", to)
hello()
name=input("What's your name? ")
hello(name) # to = name