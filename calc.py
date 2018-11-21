import math #importing this to aid with couple of calc fns
#create class for all our methods to sit inside
class Calc(object):

    def add(self, a, b):
        #function to add two numbers
        if isinstance(a,str) == True or isinstance(b, str) == True: #accounts for strings, repeat throughout
            return "Strings not allowed, please try again"
        return a + b #returns answer
    
    def cosine(self,a):
        #function to calc cos of one angle
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        rad = math.radians(a) #convert from deg to rads, assuming user will enter degrees, also hard for user to enter certain well used angles in radians exactly (90 = pi/2, etc)
        return math.cos(rad) #returns cos of converted angle
    
    def cube(self, a):
        #fn to cube one number
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        return a ** 3
    
    def cuberoot(self, a):
        #fn to get cuberoot of a number
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        elif a >= 0: #for a>0 simple case
            return a ** (1/3)
        elif a< 0:
            return -(-a) ** (1/3) #reason we need to do this is that the approximation of 1/3 power will eval to a complex number
        
    def divide(self, a, b):
        #fn to divide one number by another
        if isinstance(a,str) == True or isinstance(b, str) == True:
            return "Strings not allowed, please try again"
        elif b == 0: #accounting for divide by zero
            return "Divide by Zero not allowed"
        return a/b
    
    def exponent(self, a, b): 
        #fun to raise one number to power of another
        #this fn only works well for a>=0 as a ** b will not accurately roots that return real answers, i.e. cubed root
        if isinstance(a,str) == True or isinstance(b, str) == True:
            return "Strings not allowed, please try again"
        elif a==0 and b==0:
            return "undefined term"
        elif a < 0:
            return "this calculator cannot give an accurate answer in case a<0"
        return a ** b
        
    def factorial(self, a):
        #fn to take the factorial of a non-neg integer
        if isinstance(a, int) == False:
            return "Factorial only works on non-negative integers."
        elif a < 0:
            return "Factorial only works on non-negative integers."
        fact = 1 #for loop to calculate factorial
        for i in range(1, (a+1)):
            fact = i * fact 
        return fact
     
    def multiply(self, a, b):
        #fn to multiply two numbers
        if isinstance(a,str) == True or isinstance(b, str) == True:
            return "Strings not allowed, please try again"
        return a * b
    
    def reciprocal(self, a):
        #fn to compute reciprocal of any number 
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        if a == 0:
            return "Division by zero not allowed."
        return 1/a
    
    def sine(self, a):
        #fn to caclulate sine of an angle
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        rad = math.radians(a)  #see cosine fn above for explanation
        return math.sin(rad)
    
    def square(self, a):
        #fn to square a number
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        return a ** 2
    
    def squareroot(self, a):
        #fn to take suare root of a number. Restricted to non-neg numbers as will not be accurate for a<0 (i.e sqrt(-1) will not equal 0 exactly)
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        if a<0:
            return "We are limiting ourselves to real number answers, enter a non-negative number"
        return a ** 0.5
    
    def subtract(self, a, b):
        #fn to subtract one number from another
        if isinstance(a,str) == True or isinstance(b, str) == True:
            return "Strings not allowed, please try again"
        return a - b
    
    def tangent(self, a): 
        #fn to calculate tan of an angle
        #this function will only produce an approx of tan, it can't deal with the zeros
        if isinstance(a,str) == True:
            return "Strings not allowed, please try again"
        rad = math.radians(a)
        return (math.sin(rad) / math.cos(rad)) 



