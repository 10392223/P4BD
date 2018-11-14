#CA5 involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
#You will be required to refactor / rewrite your functions so that they can handle lists.
#You will need to use lambda, map, filter, reduce, generator, and list comprehension in any manner you deem necessary to achieve this.
#Submit a Python script of your program to moodle and github as well as any tests you have done which should still work.

#The deadline is the 18th November 2018 on moodle @ 23:55.

"I have used map, filter, reduce, generators and list comprehension in at least one function each here."


import math #importing this to aid with couple of calc fns
from functools import reduce #import reduce fn

#function to add a list of numbers together
def addList(*a):
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #if we removed strings still return sum and then give message indicating some strings were removed  
    elif len(numbers) < len(a):
    #reduce function will take our list of strings and add them all and return one value
        return reduce((lambda x, y: x+y), numbers), "We removed your strings"
    
    #else return the sum using reduce
    return reduce((lambda x, y: x+y), numbers) 
 
#function to get the cosines of a list of numbers and return answer in list
def cosList(*a):
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    angles = [math.radians(elm) for elm in numbers]
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
            
    #else return cosine list
    return list(map(lambda x: math.cos(x), angles))

def cubeList(*a):
#fn to cube list of numbers and return answers in a list
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #return message to let them know data was cleansed
    elif len(numbers) < len(a):
        return [x**3 for x in numbers], "We removed your strings"
    
    #returns if no strings in list
    return [x**3 for x in numbers]

def cuberootList(*a):
    #fn to get cuberoots of a list of numbers and return in a list
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
    #use filter to split into neg and non-neg numbers
    #we need to do this as fn for calculating cube roots is different for x>=0 and x<0 or we end up with incorrect complex values for some real valued roots
    non_neg = list(filter(lambda x: x >= 0, numbers))
    neg = list(filter(lambda x: x<0, numbers))
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #if we removed strings still return sum and then give message indicating some strings were removed  
    elif len(numbers) < len(a):
    
        #return two lists, one with cuberoots of non neg numbers, and one for neg numbers, and message to say strings filtered out
        return list(map(lambda x: x**(1/3), non_neg)), list(map(lambda x: -(-x)**(1/3), neg)), "We removed your strings" #for a>0 simple case
   
    #case for no strings removed
    return list(map(lambda x: x**(1/3), non_neg)), list(map(lambda x: -(-x)**(1/3), neg))
    
def divideLists(a, b):
    #doesn't make sense to sense to set up a rolling division here like addList fn
    #define function to be pairwise division of two lists of equal length
    if type(a) != list or type(b) != list:
        return "Please enter two lists of numbers"
    
    elif len(a) != len(b):
        "Please enter two lists of numbers of equal length"
    
    #list comprehension to remove all strings
    num_a = [elm for elm in a if isinstance(elm, str) == False]
    num_b = [elm for elm in b if isinstance(elm, str) == False or elm !=0]
    
    if len(num_a) != len(num_b):
        return "Strings or 0 in second list, please try again"
#   
    return [x/y for (x, y) in zip(a, b)]

def exponentLists(a, b): 
    
    if type(a) != list or type(b) != list:
        return "Please enter two lists of numbers"
    
    elif len(a) != len(b):
        "Please enter two lists of numbers of equal length"
        
    return [x ** y for (x, y) in zip(a, b)]
    #fn to raise one number to power of another
    #this fn only works well for a>=0 as a ** b will not accurately roots that return real answers, i.e. cubed root
#    if isinstance(a,str) == True or isinstance(b, str) == True:
#        return "Strings not allowed, please try again"
#    elif a==0 and b==0:
#        return "undefined term"
#    elif a < 0:
#        return "this calculator cannot give an accurate answer in case a<0"
#    return a ** b
    
def factorialList(*a):
    #fn to take the factorials of a list of non-neg integers
    
    return list(map((lambda n: math.factorial(n)), a))
     
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
def sineList(*a):
       
    angles = [math.radians(elm) for elm in a]
    #function to calc cos of a list of angles
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
     #convert from deg to rads, assuming user will enter degrees, also hard for user to enter certain well used angles in radians exactly (90 = pi/2, etc)
    return list(map(lambda x: math.sin(x), angles))#returns cos of converted angle
def squareList(*a):
    squares = list(a)
    #fn to square a number
#    if isinstance(a,str) == True:
#        return "Strings not allowed, please try again"
    return list(map((lambda x: x**2), squares))

def squareGenerator(*a):
    squares = list(a)
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

def tangentList(*a): 
    #fn to calculate tan of list of angles
    #this function will only produce an approx of tan, it can't deal with the zeros
    angles = [math.radians(elm) for elm in a]
    return list(map(lambda x: math.tan(x), angles))




