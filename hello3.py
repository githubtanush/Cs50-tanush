def main():
    name=input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

#but in the scope of main hello is not defined
#that's why this is not called
#but in this it is working before i call main at last
#which gives me access to call the function from anyway and 
#anywhere and give me accessibility to write code anywhere
