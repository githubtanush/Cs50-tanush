'''import statistics
print(statistics.mean([100, 90]))'''
#sys = system
'''import sys
try:
    print("hello, my name is",sys.argv[0])#index error
except IndexError:
    print("Too few arguments")'''


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