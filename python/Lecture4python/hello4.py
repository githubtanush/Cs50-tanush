'''print("hello, world") #syntax error- when we not end with commas
x=int(input("What's x? "))
print(f'x is {x}')'''
#try-keyword in python whether or not something exceptional
#except-exceptional cases error in valueerror v in value and 
# e in error must be capital

'''try:
        x=int(input("What's x? "))
        print(f'x is {x}')
except ValueError:
        print("x is not an integer")
else:
        print(f"x is {x}")'''
#control-c to terminate loop
#Name error - name is not defined properly
'''def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()'''
#pass function - use for silently pass the program don't show any meassage and prompting again and again
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
           pass

main()
#try,except,else,pass,return,break,elif,while,raise