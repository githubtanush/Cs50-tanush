'''import statistics
print(statistics.mean([100, 90]))'''
#sys = system
'''import sys
try:
    print("hello, my name is",sys.argv[0])#index error
except IndexError:
    print("Too few arguments")'''

#sys.argv[1] storing my element which i written after the filename

'''import sys
try:
    print("hello, my name is",sys.argv[1])#index error-
except IndexError:
    print("Too few arguments")'''

'''import sys
#check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")#sys.exit = to exit out from there
elif len(sys.argv) > 2:
    print("Too many arguments")
#print name tags
    print("hello, my name is", sys.argv[1])'''

'''if we write like this Tanush then next arora will be the next argument
on the other if i written like this "Tanush Arora" it will be treated as 
single word'''

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello,my name is", arg)

#slice- means to take a subset of a list
import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)