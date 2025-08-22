x=int(input("What's x? "))#when we written int at starting then we don't need to write below specifically that it is int because we mentioned already very best at upper 
y=int(input("What's y? "))
#z=int(x)+int(y)  when you not written int a will act like a string and simply only combine the letter because by default it act like a string
print(x+y)

# alternative way 
#print(int(input("What's x?")) + int(input("What's y?")))


x=float(input("What's x?"))
y=float(input("What's y?"))
z=round(x+y)
print(f"{z:,}")

x=float(input("What's x?"))
y=float(input("What's y?"))
#z=round(x/y,3)# after x,y written means that how many no. would be printed after decimal
print(f"{z:.2f}")# when u are not write in round form then u written like this directly

