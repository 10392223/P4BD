# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:52:42 2018

@author: Martin PC

"""

import unittest
from calcmapreduce import CalcMapReduce
import numpy as np

class CalcmapreduceTest(unittest.TestCase): #inherits from unittest
    
    def setUp(self):
        self.c = CalcMapReduce()
        
    def testAddList(self):
        #fn to test addList fn
        self.assertEqual(10, self.c.addList(1,2,3,4)) #test + numbers
        self.assertEqual(-10, self.c.addList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(2, self.c.addList(1,-2,3)) #test mix
        self.assertEqual(1, self.c.addList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", self.c.addList()) #test no args entered
        self.assertEqual((4, 'We removed your strings'), self.c.addList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", self.c.addList('b', 'a'))#test list with all strings
        
    def testCosList(self):
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,1,-1], self.c.cosList(90,0,180))
        self.assertEqual("No numbers in input, please try again", self.c.cosList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", self.c.cosList('b', 'a'))#test list with all strings
    
    def testCubeList(self):
        #testing cubeList function
        self.assertEqual([1,8,27], self.c.cubeList(1,2,3))#test + numbers
        self.assertEqual([-1,-8,-27], self.c.cubeList(-1,-2,-3))#test - numbers
        self.assertEqual([1,-8,27], self.c.cubeList(1,-2,3)) #test mix
        self.assertEqual([1], self.c.cubeList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", self.c.cubeList()) #test no args entered
        self.assertEqual(([1,27], 'We removed your strings'), self.c.cubeList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", self.c.cubeList('b', 'a'))#test list with all strings
        
    def testCuberootList(self): #test cuberootList fn
        
        self.assertEqual(([1, 3, 2], []), self.c.cuberootList(1,27,8))#test + numbers
        self.assertEqual(([],[-1,-2,-3]), self.c.cuberootList(-1,-8,-27))#test - numbers
        self.assertEqual(([1],[-2]), self.c.cuberootList(1,-8)) #test mix
        self.assertEqual(([1],[]), self.c.cuberootList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", self.c.cuberootList()) #test no args entered
        self.assertEqual(([1,3],[], 'We removed your strings'), self.c.cuberootList(1,'a',27))#test list with string
        self.assertEqual("No numbers in input, please try again", self.c.cuberootList('b', 'a'))#test list with all strings
        
    def testDivideLists(self): #test divideLists fn
        
        self.assertEqual([2,2], self.c.divideLists([4,2], [2,1])) #test example that works normally
        self.assertEqual("Strings or 0 in second list, please try again", self.c.divideLists([4,2], [2,0])) #check div/0
        self.assertEqual([2,0], self.c.divideLists([4,0], [2,2])) #check 0 in first list
        self.assertEqual("Strings or 0 in second list, please try again", self.c.divideLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", self.c.divideLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", self.c.divideLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", self.c.divideLists([], [])) #check empty lists
        self.assertEqual("Strings or 0 in second list, please try again", self.c.divideLists([4,2], ['a',0])) #check string and div/0 to make sure if if statement in list comp is working
    
    def testExponentLists(self):
     #test exponentLists function
     
        self.assertEqual([1,4], self.c.exponentLists([1,2], [2,2])) #test example that works normally
        self.assertEqual("Strings or a<0, please try again", self.c.exponentLists([-1,2], [2,2])) #check a<0
        self.assertEqual([16,1], self.c.exponentLists([4,1], [2,0])) #check b<0
        self.assertEqual("Strings or a<0, please try again", self.c.exponentLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", self.c.exponentLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", self.c.exponentLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", self.c.exponentLists([], [])) #check empty lists
        self.assertEqual("Strings or a<0, please try again", self.c.exponentLists(['a',0],[4,2])) #check string and a<0 to make sure combo works
        
    def testFactorialList(self): #function to test factorialList
        
        self.assertEqual([1,2,6], self.c.factorialList(1,2,3)) #regular inputs that return valid calculation           
        self.assertEqual("No valid numbers in input, please try again", self.c.factorialList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(([1,6], "We removed all but non-negative ints from your inputs"), self.c.factorialList(1,-2,3)) #test mix
        self.assertEqual("No valid numbers in input, please try again", self.c.factorialList()) #test no args entered
        self.assertEqual(([1,6], "We removed all but non-negative ints from your inputs"), self.c.factorialList(1,'a',3))#test list with string
        self.assertEqual("No valid numbers in input, please try again", self.c.factorialList('b', 'a'))#test list with all strings
        self.assertEqual(([24], "We removed all but non-negative ints from your inputs"), self.c.factorialList(1.3, 4, 'a'))#test list float, str
        
    def testMultiplyList(self): #fn to test multiplyList fn
        
        self.assertEqual(6, self.c.multiplyList(1,2,3)) #test + numbers
        self.assertEqual(24, self.c.multiplyList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(-6, self.c.multiplyList(1,-2,3)) #test mix
        self.assertEqual(1, self.c.multiplyList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", self.c.multiplyList()) #test no args entered
        self.assertEqual((3, 'We removed your strings'), self.c.multiplyList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", self.c.multiplyList('b', 'a'))#test list with all strings
        
    def testReciprocalList(self): #fn to test reciprocalList
        
        self.assertEqual([1,0.5, 0.25], self.c.reciprocalList(1,2,4)) #test + numbers
        self.assertEqual([-1,-0.5, -1/3], self.c.reciprocalList(-1,-2,-3))#test - numbers       
        self.assertEqual([1,-0.5,1/3], self.c.reciprocalList(1,-2,3)) #test mix
        self.assertEqual([1], self.c.reciprocalList(1)) #test just one
        self.assertEqual("No valid numbers in input, please try again", self.c.reciprocalList()) #test no args entered
        self.assertEqual(([1,1/3], "We removed your strings or any 0s"), self.c.reciprocalList(1,'a',3))#test list with string
        self.assertEqual("No valid numbers in input, please try again", self.c.reciprocalList('b', 'a'))#test list with all strings
        self.assertEqual(([1],"We removed your strings or any 0s"), self.c.reciprocalList(0, 1))#test 0
        self.assertEqual(("No valid numbers in input, please try again"), self.c.reciprocalList(0, 'str'))#test 0 and string
     
    def testSineList(self):#fn to test sineList fn
        
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([1,0,0], self.c.sineList(90,0,180))
        self.assertEqual("No numbers in input, please try again", self.c.sineList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", self.c.sineList('b', 'a'))#test list with all strings
        
    def testSquareList(self): #fn to test squareList
        
        self.assertEqual([1,4,9], self.c.squareList(1,2,3))#test + numbers
        self.assertEqual([1,4,9], self.c.squareList(-1,-2,-3))#test - numbers
        self.assertEqual([1,4,9], self.c.squareList(1,-2,3)) #test mix
        self.assertEqual([1], self.c.squareList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", self.c.squareList()) #test no args entered
        self.assertEqual(([1,9], 'We removed your strings'), self.c.squareList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", self.c.squareList('b', 'a'))#test list with all strings
        
   
        
    def testSquareGenerator(self): #fn to test squareGenerator
        
        #set up the generator with some inputs
        
        self.square = self.c.squareGenerator(1,2,3)
        #test that each iteration works
        self.assertEqual(1, next(self.square))
        self.assertEqual(4, next(self.square))
        self.assertEqual(9, next(self.square))
           
        self.square = self.c.squareGenerator(1,'a',3)
        self.assertEqual(1, next(self.square))#test list with string
        self.assertEqual(9, next(self.square))
                
        
    def testSquarerootList(self): #fn to test squarerootList fn
        
           
        self.assertEqual([1,2], self.c.squarerootList(1,4))#test + numbers
        self.assertEqual("No valid numbers in input, please try again", self.c.squarerootList(-1))#test - numbers
        self.assertEqual(([1,2], "Removed strings or numbers less than 0"),self.c.squarerootList(1,-4,4)) #test mix
        self.assertEqual([1], self.c.squarerootList(1)) #test just one
        self.assertEqual("No valid numbers in input, please try again", self.c.squarerootList()) #test no args entered
        self.assertEqual(([1,3], "Removed strings or numbers less than 0"), self.c.squarerootList(1,'a',9))#test list with string
        self.assertEqual("No valid numbers in input, please try again", self.c.squarerootList('b', 'a'))#test list with all strings
        
    def testSubtractLists(self): #fn to test SubtractLists fn
        
        self.assertEqual([1,1], self.c.subtractLists([2,2], [1,1])) #test example that works normally
        self.assertEqual("Strings found in lists, please try again", self.c.subtractLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", self.c.subtractLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", self.c.subtractLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", self.c.subtractLists([], [])) #check empty lists
        self.assertEqual("Strings found in lists, please try again", self.c.subtractLists([4,2], ['a',0])) #check string and div/0 to make sure if if statement in list comp is working
        
    def testTanList(self): #test for tangetList fn
        
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,0], self.c.tangentList(0,180))
        self.assertEqual("No numbers in input, please try again", self.c.tangentList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", self.c.tangentList('b', 'a'))#test list with all strings

if __name__ == '__main__':        
    unittest.main()