#modules - A module is python in a library typically has one or
#more functions or other features built into it. Generally , the 
#purpose of the library or a module specifically is a reusability 
#of code if u want to use any function again and again then u must 
# be copy and pasting it into library and then we use


# python come with different libraries :- 
# random 
# import keyword in python allows you to import components

'''import random # means i import the random library
coin = random.choice(["heads","tails"])# means like randomly choose heads or tails
print(coin)'''
#import - to use another python code as a library function and small our code
#random - it is a function  which is used as a function randomly
#from - it is a keyword in python from is a keyword in python it is used for impoting functions from a module but it allows to be a little more specific
'''from random import choice
coin = choice(["heads","tails"])'''


'''import random
number = random.randint(1,10)#randint means randomly any integer is written
print(number)'''

import random
cards = ["jack","queen","king"]
random.shuffle(cards)# means shuffle randomly
for card in cards:
    print(card)