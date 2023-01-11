'''import random
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
random.shuffle(cards)
for card in cards:
    print(card)