#Syntax Error -> Syntax error is the problem that i can do write 
#in syntax it just must be fix;
print("hello, world")


#Value Error -> when we write anything for example we want to take 
#the input in integer but i will take input of string then it will 
#be value error
x = int ( input ("What's x ? ") )
print(f"x is {x}")

#python has these keyword try to check whether there is some exceptional 
#or not

#NameError means that name is not defined may be out of scope or anyother 
#thing happen
# UnboundLocalError: local variable 'x' referenced before assignment

while True:
    try:
        x = int(input("What's x? "))
    except ValueError: 
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else: 
            break
    return x

main()