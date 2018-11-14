# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:52:42 2018

@author: Martin PC

"""

import unittest
from calcmapreduce import addList, cosList, cubeList, cuberootList, divideLists, exponentLists, factorialList, multiplyList, reciprocalList, sineList, squareList, squareGenerator, squarerootList, subtractLists, tangentList
import numpy as np

class CalcmapreduceTest(unittest.TestCase): #inherits from unittest
    
    def testAddList(self):
        #fn to test addList fn
        self.assertEqual(10, addList(1,2,3,4)) #test + numbers
        self.assertEqual(-10, addList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(2, addList(1,-2,3)) #test mix
        self.assertEqual(1, addList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", addList()) #test no args entered
        self.assertEqual((4, 'We removed your strings'), addList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", addList('b', 'a'))#test list with all strings
        
    def testCosList(self):
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,1,-1], cosList(90,0,180))
        self.assertEqual("No numbers in input, please try again", cosList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", cosList('b', 'a'))#test list with all strings
    
    def testCubeList(self):
        #testing cubeList function
        self.assertEqual([1,8,27], cubeList(1,2,3))#test + numbers
        self.assertEqual([-1,-8,-27], cubeList(-1,-2,-3))#test - numbers
        self.assertEqual([1,-8,27], cubeList(1,-2,3)) #test mix
        self.assertEqual([1], cubeList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", cubeList()) #test no args entered
        self.assertEqual(([1,27], 'We removed your strings'), cubeList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", cubeList('b', 'a'))#test list with all strings
        
    def testCuberootList(self): #test cuberootList fn
        
        self.assertEqual(([1, 3, 2], []), cuberootList(1,27,8))#test + numbers
        self.assertEqual(([],[-1,-2,-3]), cuberootList(-1,-8,-27))#test - numbers
        self.assertEqual(([1],[-2]), cuberootList(1,-8)) #test mix
        self.assertEqual(([1],[]), cuberootList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", cuberootList()) #test no args entered
        self.assertEqual(([1,3],[], 'We removed your strings'), cuberootList(1,'a',27))#test list with string
        self.assertEqual("No numbers in input, please try again", cuberootList('b', 'a'))#test list with all strings
        
    def testDivideLists(self): #test divideLists fn
        
        self.assertEqual([2,2], divideLists([4,2], [2,1])) #test example that works normally
        self.assertEqual("Strings or 0 in second list, please try again", divideLists([4,2], [2,0])) #check div/0
        self.assertEqual([2,0], divideLists([4,0], [2,2])) #check 0 in first list
        self.assertEqual("Strings or 0 in second list, please try again", divideLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", divideLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", divideLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", divideLists([], [])) #check empty lists
        self.assertEqual("Strings or 0 in second list, please try again", divideLists([4,2], ['a',0])) #check string and div/0 to make sure if if statement in list comp is working
    
    def testExponentLists(self):
     #test exponentLists function
     
        self.assertEqual([1,4], exponentLists([1,2], [2,2])) #test example that works normally
        self.assertEqual("Strings or a<0, please try again", exponentLists([-1,2], [2,2])) #check a<0
        self.assertEqual([16,1], exponentLists([4,1], [2,0])) #check b<0
        self.assertEqual("Strings or a<0, please try again", exponentLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", exponentLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", exponentLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", exponentLists([], [])) #check empty lists
        self.assertEqual("Strings or a<0, please try again", exponentLists(['a',0],[4,2])) #check string and a<0 to make sure combo works
        
    def testFactorialList(self): #function to test factorialList
        
        self.assertEqual([1,2,6], factorialList(1,2,3)) #regular inputs that return valid calculation           
        self.assertEqual("No valid numbers in input, please try again", factorialList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(([1,6], "We removed all but non-negative ints from your inputs"), factorialList(1,-2,3)) #test mix
        self.assertEqual("No valid numbers in input, please try again", factorialList()) #test no args entered
        self.assertEqual(([1,6], "We removed all but non-negative ints from your inputs"), factorialList(1,'a',3))#test list with string
        self.assertEqual("No valid numbers in input, please try again", factorialList('b', 'a'))#test list with all strings
        self.assertEqual(([24], "We removed all but non-negative ints from your inputs"), factorialList(1.3, 4, 'a'))#test list float, str
        
    def testMultiplyList(self): #fn to test multiplyList fn
        
        self.assertEqual(6, multiplyList(1,2,3)) #test + numbers
        self.assertEqual(24, multiplyList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(-6, multiplyList(1,-2,3)) #test mix
        self.assertEqual(1, multiplyList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", multiplyList()) #test no args entered
        self.assertEqual((3, 'We removed your strings'), multiplyList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", multiplyList('b', 'a'))#test list with all strings
        
    def testReciprocalList(self): #fn to test reciprocalList
        
        self.assertEqual([1,0.5, 0.25], reciprocalList(1,2,4)) #test + numbers
        self.assertEqual([-1,-0.5, -1/3], reciprocalList(-1,-2,-3))#test - numbers       
        self.assertEqual([1,-0.5,1/3], reciprocalList(1,-2,3)) #test mix
        self.assertEqual([1], reciprocalList(1)) #test just one
        self.assertEqual("No valid numbers in input, please try again", reciprocalList()) #test no args entered
        self.assertEqual(([1,1/3], "We removed your strings or any 0s"), reciprocalList(1,'a',3))#test list with string
        self.assertEqual("No valid numbers in input, please try again", reciprocalList('b', 'a'))#test list with all strings
        self.assertEqual(([1],"We removed your strings or any 0s"), reciprocalList(0, 1))#test 0
        self.assertEqual(("No valid numbers in input, please try again"), reciprocalList(0, 'str'))#test 0 and string
     
    def testSineList(self):#fn to test sineList fn
        
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([1,0,0], sineList(90,0,180))
        self.assertEqual("No numbers in input, please try again", sineList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", sineList('b', 'a'))#test list with all strings
        
    def testSquareList(self): #fn to test squareList
        
        self.assertEqual([1,4,9], squareList(1,2,3))#test + numbers
        self.assertEqual([1,4,9], squareList(-1,-2,-3))#test - numbers
        self.assertEqual([1,4,9], squareList(1,-2,3)) #test mix
        self.assertEqual([1], squareList(1)) #test just one
        self.assertEqual("No numbers in input, please try again", squareList()) #test no args entered
        self.assertEqual(([1,9], 'We removed your strings'), squareList(1,'a',3))#test list with string
        self.assertEqual("No numbers in input, please try again", squareList('b', 'a'))#test list with all strings
        
   
        
    def testSquareGenerator(self): #fn to test squareGenerator
        
        #set up the generator with some inputs
        
        square = squareGenerator(1,2,3)
        #test that each iteration works
        self.assertEqual(1, next(square))
        self.assertEqual(4, next(square))
        self.assertEqual(9, next(square))
           
        square = squareGenerator(1,'a',3)
        self.assertEqual(1, next(square))#test list with string
        self.assertEqual(9, next(square))
                
        
    def testSquarerootList(self): #fn to test squarerootList fn
        
           
        self.assertEqual([1,2], squarerootList(1,4))#test + numbers
        self.assertEqual("No valid numbers in input, please try again", squarerootList(-1))#test - numbers
        self.assertEqual(([1,2], "Removed strings or numbers less than 0"),squarerootList(1,-4,4)) #test mix
        self.assertEqual([1], squarerootList(1)) #test just one
        self.assertEqual("No valid numbers in input, please try again", squarerootList()) #test no args entered
        self.assertEqual(([1,3], "Removed strings or numbers less than 0"), squarerootList(1,'a',9))#test list with string
        self.assertEqual("No valid numbers in input, please try again", squarerootList('b', 'a'))#test list with all strings
        
    def testSubtractLists(self): #fn to test SubtractLists fn
        
        self.assertEqual([1,1], subtractLists([2,2], [1,1])) #test example that works normally
        self.assertEqual("Strings found in lists, please try again", subtractLists([4,2], [2,'a'])) #check strings
        self.assertEqual("Please enter two lists of numbers", subtractLists(1,2)) #check non list input
        self.assertEqual("Please enter two lists of numbers of equal length", subtractLists([1], [1,2])) #check list length doesn't match
        self.assertEqual("Lists are empty, try again", subtractLists([], [])) #check empty lists
        self.assertEqual("Strings found in lists, please try again", subtractLists([4,2], ['a',0])) #check string and div/0 to make sure if if statement in list comp is working
        
    def testTanList(self): #test for tangetList fn
        
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,0], tangentList(0,180))
        self.assertEqual("No numbers in input, please try again", tangentList()) #test no args entered
        self.assertEqual("No numbers in input, please try again", tangentList('b', 'a'))#test list with all strings

if __name__ == '__main__':        
    unittest.main()