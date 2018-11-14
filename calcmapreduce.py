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
    #convert to radians, take input in degrees as difficult to enter meaningful angles exactly i.e. pi/2, etc
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
    
    #if args aren't lists give error message
    if type(a) != list or type(b) != list:
        return "Please enter two lists of numbers"
    
    #two lists of unequal length can't be pairwise subtracted
    elif len(a) != len(b):
        return "Please enter two lists of numbers of equal length"
     
    #if two empty lists are entered return error
    elif len(a) == 0 and len(b) == 0:
        return "Lists are empty, try again"
    
    #list comprehension to remove all strings and 0s from second list to avoid div/0
    num_a = [elm for elm in a if isinstance(elm, str) == False]
    num_b = [elm for elm in b if isinstance(elm, str) == False if elm != 0]
   
    
    #check if strings have been removed or a 0 is in second list, don't want to compute in this case
    if len(num_a) != len(num_b):
        return "Strings or 0 in second list, please try again"
    
    #return pairwise division using zip function and list comprehension 
    return [x/y for (x, y) in zip(num_a, num_b)]

def exponentLists(a, b): 
#function to take in two lists and do pairwise exponentation on them. i.e exponentLists([x_1, x_2],[y_1,y_2]) = [x_1^y_1, x_2^y_2]
    
    
    #if args aren't lists give error message
    if type(a) != list or type(b) != list:
        return "Please enter two lists of numbers"
    
    #two lists of unequal length can't be pairwise subtracted
    elif len(a) != len(b):
        return "Please enter two lists of numbers of equal length"
     
    #if two empty lists are entered return error
    elif len(a) == 0 and len(b) == 0:
        return "Lists are empty, try again"
    
        #list comprehension to remove all strings and neg numbers from first list to avoid calculating a^b where a is 0 (cannot be done accurately using this calc, see my assignment 1 for rational)
    num_a = [elm for elm in a if isinstance(elm, str) == False if elm >=0]
    num_b = [elm for elm in b if isinstance(elm, str) == False]
   
    
    #check if strings have been removed or neg number in first list, don't want to compute in this case
    if len(num_a) != len(num_b):
        return "Strings or a<0, please try again"
        
    return [x ** y for (x, y) in zip(num_a,num_b)]
        
def factorialList(*a):
    #fn to take the factorials of a list of non-neg integers and return in a list
    
    #list comprehension to remove everything bar integers >=0
    numbers = [elm for elm in a if isinstance(elm, int) == True if elm>=0]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No valid numbers in input, please try again"
    #if we removed strings, floats or neg ints still return sum and then give message indicating some strings were removed  
    elif len(numbers) < len(a):
        #map function gives us list of factorials, plus message to say list was parsed
        return list(map((lambda n: math.factorial(n)), numbers)), "We removed all but non-negative ints from your inputs"
    
    return list(map((lambda n: math.factorial(n)), numbers))
     
def multiplyList(*a): #fn to multiply a list of numbers and return the product
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #if we removed strings still return product and then give message indicating some strings were removed  
    elif len(numbers) < len(a):
        #return product using reduce on the filtered list
        return reduce((lambda x,y: x*y), numbers), "We removed your strings"
    
    return reduce((lambda x,y: x*y), numbers)


def reciprocalList(*a): #fn to compute reciprocal of list of numbers and return answers in a list
        
    #list comprehension to remove all strings and any 0s to avoid div/0
    numbers = [elm for elm in a if isinstance(elm, str) == False if elm !=0]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No valid numbers in input, please try again"
    
    #return message to let them know data was cleansed of strings and 0
    elif len(numbers) < len(a):
        #return list using map function of reciprocals, minus str/0
        return list(map((lambda x: 1/x), numbers)), "We removed your strings or any 0s"
    
    
    return list(map((lambda x: 1/x), numbers))
        
def sineList(*a): #convert list of angles into list of sine of angles
    
    #list comprehension to remove all strings   
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    #convert to radians, take input in degrees as difficult to enter meaningful angles exactly i.e. pi/2, etc
    angles = [math.radians(elm) for elm in numbers]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    return list(map(lambda x: math.sin(x), angles))#returns sin of converted angle using map function

def squareList(*a): #function that squares every number in a list and returns that in a list
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #return message to let them know data was cleansed
    elif len(numbers) < len(a):
        #list comprehension to compute list of squares
        return [x**2 for x in numbers], "We removed your strings"
       
    return [x**2 for x in numbers]

def squareGenerator(*a): #function to generate a repeated square from list of inputs
    
    #list comprehension to remove all strings
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    
#set up generator with yield. now once you instatiate, you can run the generator again and again using next function      
    for value in numbers:
        yield value**2       
    

def squarerootList(*a):
    #fn to take suare roots of a list of number. Restricted to non-neg numbers as will not be accurate for a<0 (i.e sqrt(-1) will not equal i exactly
#   
#list comprehension to remove all strings and neg numbers
    numbers = [elm for elm in a if isinstance(elm, str) == False if elm>=0]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No valid numbers in input, please try again"
    
    #return message to let them know data was cleansed
    elif len(numbers) < len(a): 
        return list(map(lambda x: x**(0.5), numbers)), "Removed strings or numbers less than 0"
    
    return list(map(lambda x: x**(0.5), numbers))

def subtractLists(a, b):
    #doesn't make sense to sense to set up a rolling subtraction here.
    #define function to be pairwise subtraction of two lists of equal length

    #if args aren't lists give error message
    if type(a) != list or type(b) != list:
        return "Please enter two lists of numbers"
    
    #two lists of unequal length can't be pairwise subtracted
    elif len(a) != len(b):
        return "Please enter two lists of numbers of equal length"
     
    #if two empty lists are entered return error
    elif len(a) == 0 and len(b) == 0:
        return "Lists are empty, try again"
    
    #list comprehension to remove all strings
    num_a = [elm for elm in a if isinstance(elm, str) == False]
    num_b = [elm for elm in b if isinstance(elm, str) == False]
   
    
    #check if strings have been removed or a 0 is in second list, don't want to compute in this case
    if len(num_a) != len(num_b):
        return "Strings found in lists, please try again"

    #use list comprehehsion and zip function to create 3rd list that is the pairwise subtraction
    return [x - y for (x, y) in zip(num_a, num_b)]
 
def tangentList(*a):  #convert list of angles into list of tan of angles
    #note that this function doesn't evaluate the zeros of tan properly
    
    #list comprehension to remove all strings   
    numbers = [elm for elm in a if isinstance(elm, str) == False]
    #convert to radians, take input in degrees as difficult to enter meaningful angles exactly i.e. pi/2, etc
    angles = [math.radians(elm) for elm in numbers]
    
    #if length of list is 0 return error
    if len(numbers) == 0:
        return "No numbers in input, please try again"
    
    #return tan of angles in a list using map function
    return list(map(lambda x: math.tan(x), angles))




