def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    '''if n%2==0:
        return True
    else:
        return False'''
    #return True if n%2==0 else False
    return n%2==0
main()

'''if x%2 == 0:
    print("Even")
else:
    print("Odd")'''

