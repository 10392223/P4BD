import unittest #in built class in python for unit testing

from calc import Calc

class CalcTest(unittest.TestCase): #inherits from unittest
    
    def setUp(self):
        self.c = Calc()
        
    def testAdd(self):
        #fn to test add fn
        self.assertEqual(3, self.c.add(1,2)) #test adding 2 pos numbers
        self.assertEqual(2, self.c.add(-1, 3)) #test 1st neg, 2nd pos
        self.assertEqual(4.5, self.c.add(6, -1.5)) #test 1st pos, 2nd neg
        self.assertEqual(-4, self.c.add(-2, -2)) #test both neg
        self.assertEqual("Strings not allowed, please try again", self.c.add("two", "three")) #test if we get error with two strings
        self.assertEqual("Strings not allowed, please try again", self.c.add(2, "three")) #test if we get error with int, str args
        self.assertEqual("Strings not allowed, please try again", self.c.add("two", 3)) #test if we get error with str, int args
      
    def testCosine(self):
        #fn to test cosine fn
        self.assertAlmostEqual(0, self.c.cosine(90)) #need to use almost equal here as there is a loss of accuracy i.e the function is calculating cos(90) to be close to zero, not identically equal to it
        self.assertAlmostEqual(0, self.c.cosine(-90))
        self.assertAlmostEqual(1, self.c.cosine(0))
        self.assertEqual("Strings not allowed, please try again", self.c.cosine("90")) #test if we get error with string
     
    def testCube(self):
        #fn to test cube fn
        self.assertEqual(8, self.c.cube(2))
        self.assertEqual(-8, self.c.cube(-2))
        self.assertEqual("Strings not allowed, please try again", self.c.cube("0"))
        
    def testCubeRoot(self):
        #fn to test cube root fn
        self.assertEqual(2, self.c.cuberoot(8))
        self.assertAlmostEqual(-2, self.c.cuberoot(-8))
        self.assertEqual("Strings not allowed, please try again", self.c.cube("0"))

    def testDivide(self):
        #fn to test divide fn
        self.assertEqual(0.5, self.c.divide(1,2)) 
        self.assertEqual(-1, self.c.divide(-3, 3))
        self.assertEqual(-4, self.c.divide(6, -1.5))
        self.assertEqual(1, self.c.divide(-2, -2))
        self.assertEqual("Divide by Zero not allowed", self.c.divide(3,0))
        self.assertEqual("Strings not allowed, please try again", self.c.divide("two", "three")) #test if we get error with two strings
        self.assertEqual("Strings not allowed, please try again", self.c.divide(2, "three")) #test if we get error with int, str args
        self.assertEqual("Strings not allowed, please try again", self.c.divide("two", 3)) #test if we get error with str, int args
        
    def testExponent(self):
        #fn to test exponent fn
        self.assertEqual(8, self.c.exponent(2, 3)) #testing combinations of values
        self.assertEqual(2, self.c.exponent(8, 1/3))
        self.assertEqual(0.125, self.c.exponent(0.5, 3))
        self.assertEqual(0.5, self.c.exponent(2, -1))
        self.assertEqual("undefined term", self.c.exponent(0,0)) #for case a, b =0
        self.assertEqual("this calculator cannot give an accurate answer in case a<0", self.c.exponent(-1, 3))
        self.assertEqual("Strings not allowed, please try again", self.c.exponent("two", "three")) #test if we get error with two strings
        self.assertEqual("Strings not allowed, please try again", self.c.exponent(2, "three")) #test if we get error with int, str args
        self.assertEqual("Strings not allowed, please try again", self.c.exponent("two", 3))
        
    def testFactorial(self):
        #fn to test factorial fn
        self.assertEqual(120, self.c.factorial(5))
        self.assertEqual(1, self.c.factorial(0)) #testing definitoon of 0! to be 1
        self.assertEqual("Factorial only works on non-negative integers.", self.c.factorial(-2))
        self.assertEqual("Factorial only works on non-negative integers.", self.c.factorial(1.2))
        self.assertEqual("Factorial only works on non-negative integers.", self.c.factorial("12"))
    
    def testMultiply(self):
        #fn to test multiply fn
        self.assertEqual(2, self.c.multiply(1,2)) #test mult 2 pos numbers
        self.assertEqual(-9, self.c.multiply(-3, 3)) #test 1st neg, 2nd pos
        self.assertEqual(-9, self.c.multiply(6, -1.5)) #test 1st pos, 2nd neg
        self.assertEqual(4, self.c.multiply(-2, -2))
        self.assertEqual("Strings not allowed, please try again", self.c.multiply("two", "three")) #test if we get error with two strings
        self.assertEqual("Strings not allowed, please try again", self.c.multiply(2, "three")) #test if we get error with int, str args
        self.assertEqual("Strings not allowed, please try again", self.c.multiply("two", 3)) #test if we get error with str, int args
        
    def testReciprocal(self):
        #fn to test reciprocal fn
        self.assertEqual(0.5, self.c.reciprocal(2))
        self.assertEqual(-0.5, self.c.reciprocal(-2))
        self.assertEqual("Division by zero not allowed.", self.c.reciprocal(0))
        self.assertEqual("Strings not allowed, please try again", self.c.reciprocal("2"))
        
    def testSine(self):
        #fn to test sine fn
        self.assertAlmostEqual(1, self.c.sine(90)) #need to use almost equal here as there is a loss of accuracy i.e the function is calculating cos(90) to be close to zero, not identically equal to it
        self.assertAlmostEqual(-1, self.c.sine(-90))
        self.assertAlmostEqual(0, self.c.sine(0))
        self.assertEqual("Strings not allowed, please try again", self.c.sine("90")) #test if we get error with string
     
    def testSquare(self):
        #fn to test square fn
        self.assertEqual(4, self.c.square(2))
        self.assertEqual(4, self.c.square(-2))
        self.assertEqual("Strings not allowed, please try again", self.c.square("90"))
        
    def testSquareRoot(self):
        #fn to test square root fn
        self.assertEqual(2, self.c.squareroot(4))
        self.assertEqual("We are limiting ourselves to real number answers, enter a non-negative number", self.c.squareroot(-1))
        self.assertEqual("Strings not allowed, please try again", self.c.squareroot("90"))
        
    def testSubtract(self):
        #fn to test subtract fn
        self.assertEqual(1, self.c.subtract(2,1)) #test a>b
        self.assertEqual(-6, self.c.subtract(-3, 3)) #test a<b
        self.assertEqual("Strings not allowed, please try again", self.c.subtract("two", "three")) #test if we get error with two strings
        self.assertEqual("Strings not allowed, please try again", self.c.subtract(2, "three")) #test if we get error with int, str args
        self.assertEqual("Strings not allowed, please try again", self.c.subtract("two", 3)) #test if we get error with str, int args
      
    def testTangent(self):
        #fn to test tangent fn
        self.assertAlmostEqual(0, self.c.tangent(0))
        self.assertAlmostEqual(0, self.c.tangent(180))
        self.assertAlmostEqual(0, self.c.tangent(-180))
        self.assertEqual("Strings not allowed, please try again", self.c.tangent("90")) #test if we get error with string

if __name__ == '__main__':      
    unittest.main()