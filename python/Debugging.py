def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * i)


if __name__=="__main__":
    main()

#breakpoints are important that we can see how where we are break the program