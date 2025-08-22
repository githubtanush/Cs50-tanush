'''print("meow")
print("meow")
print("meow")'''
#use of while loop
'''i = 3
while i != 0: #control-c is a shortcut key to stop infinite loop in terminal
    print("meow")
    i -= 1'''
'''i=0
while i < 3:
    print("meow")
    i+=1'''


# use of for loop
'''for i in range(10):
    print("meow")'''

'''print("meow\n"*3,end="")'''

'''while True:
    n=int(input("What's n?"))
    if n>0:
        break #break is used to break a loop in between

for _ in range(n):
    print("meow")'''


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("What's n? "))
        if n>0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")

main()