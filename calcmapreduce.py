#CA5 involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
#You will be required to refactor / rewrite your functions so that they can handle lists.
#You will need to use lambda, map, filter, reduce, generator, and list comprehension in any manner you deem necessary to achieve this.
#Submit a Python script of your program to moodle and github as well as any tests you have done which should still work.

#The deadline is the 18th November 2018 on moodle @ 23:55.

import math #importing this to aid with couple of calc fns
from functools import reduce

def addList(*a):
    #function to add a list of numbers together
    add = list(a)
    for item in add:
        if isinstance(item,str) == True: #accounts for strings, repeat throughout
            return "Strings not allowed, please try again"
    
    return reduce((lambda x, y: x+y), add)
    
 
    
    
    


def cosList(*a):
    angles = list(a)
    #function to calc cos of a list of angles
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
    rad = math.radians(angles) #convert from deg to rads, assuming user will enter degrees, also hard for user to enter certain well used angles in radians exactly (90 = pi/2, etc)
    return list(map(lambda x: math.cos(x), rad))#returns cos of converted angle

def cubeList(*args):
    cubeList = list(args)
    #fn to cube one number
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
    #using list comprehension for this example
    return [x**3 for x in cubeList]

def cuberoot(a):
    #fn to get cuberoot of a number
    if isinstance(a,str) == True:
        return "Strings not allowed, please try again"
    elif a >= 0: #for a>0 simple case
        return a ** (1/3)
    elif a< 0:
        return -(-a) ** (1/3) #reason we need to do this is that the approximation of 1/3 power will eval to a complex number
    
def divideLists(a, b):
    #doesn't make sense to sense to set up a rolling division here.
    #define function to be pairwise division of two lists of equal length
#    if isinstance(a,str) == True or isinstance(b, str) == True:
#        return "Strings not allowed, please try again"
#    elif b == 0: #accounting for divide by zero
#        return "Divide by Zero not allowed"
    return [x/y for (x, y) in zip(a, b)]

def exponent(a, b): 
    #fn to raise one number to power of another
    #this fn only works well for a>=0 as a ** b will not accurately roots that return real answers, i.e. cubed root
    if isinstance(a,str) == True or isinstance(b, str) == True:
        return "Strings not allowed, please try again"
    elif a==0 and b==0:
        return "undefined term"
    elif a < 0:
        return "this calculator cannot give an accurate answer in case a<0"
    return a ** b
    
#def factorialList(*args):
#    #fn to take the factorials of a list of non-neg integers
#    fact = list(args)
#    if isinstance(a, int) == False:
#        return "Factorial only works on non-negative integers."
#    elif a < 0:
#        return "Factorial only works on non-negative integers."
#    fact = 1 #for loop to calculate factorial
#    for i in range(1, (a+1)):
#        fact = i * fact 
#    return fact
 
def multiplyList(*args):
    mult = list(args)
    #fn to multiply two numbers
#    if isinstance(a,str) == True or isinstance(b, str) == True:
#        return "Strings not allowed, please try again"
    return reduce((lambda x,y: x*y), mult)

def reciprocalList(*args):
    recip = list(args)
    #fn to compute reciprocal of any number 
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
#    if a == 0:
#        return "Division by zero not allowed."
    return list(map((lambda x: 1/x), recip))
def sine(a):
    #fn to caclulate sine of an angle
    if isinstance(a,str) == True:
        return "Strings not allowed, please try again"
    rad = math.radians(a)  #see cosine fn above for explanation
    return math.sin(rad)

def squareList(*args):
    squares = list(args)
    #fn to square a number
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
    return list(map((lambda x: x**2), squares))

def squareGenerator(squares):
    for value in squares:
        yield value**2
        
    

def squarerootList(*a):
    #fn to take suare root of a number. Restricted to non-neg numbers as will not be accurate for a<0 (i.e sqrt(-1) will not equal 0 exactly)
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
#    if a<0:
#        return "We are limiting ourselves to real number answers, enter a non-negative number"
    roots = list(a)
    non_neg = list(filter(lambda x: x >= 0, roots))
#    if len(less_than_zero) < len(roots):
#        print("We filtered negative numbers out of your list")
    return list(map(lambda x: x**(0.5), non_neg))

def subtractLists(a, b):
    #doesn't make sense to sense to set up a rolling subtraction here.
    #define function to be pairwise subtraction of two lists of equal length
#    if isinstance(a,str) == True or isinstance(b, str) == True:
#        return "Strings not allowed, please try again"
    #use list comprehehsion and zip function to create 3rd list that is the pairwise subtraction
    return [x - y for (x, y) in zip(a, b)]

def tangent(a): 
    #fn to calculate tan of an angle
    #this function will only produce an approx of tan, it can't deal with the zeros
    if isinstance(a,str) == True:
        return "Strings not allowed, please try again"
    rad = math.radians(a)
    return (math.sin(rad) / math.cos(rad)) 



