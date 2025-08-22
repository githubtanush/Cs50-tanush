'''import cowsay #cowsay is a program which first download then they will apply
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, "+ sys.argv[1])

#JSON=java script object notation
'''
import sys
from python.Lecture1python.sayings import hello

if len(sys.argv)==2:
    hello(sys.argv[1])
    