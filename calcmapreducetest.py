# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:52:42 2018

@author: Martin PC

"""

import unittest
from calcmapreduce import addList, cosList, cubeList, cuberootList, divideLists, factorialList, multiplyList, reciprocalList, sineList, squareList, squareGenerator, squarerootList, subtractLists, tangentList
import numpy as np

class CalcmapreduceTest(unittest.TestCase): #inherits from unittest
    
    def testAddList(self):
        #fn to test add fn
        self.assertEqual(10, addList(1,2,3,4)) #test + numbers
        self.assertEqual(-10, addList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(2, addList(1,-2,3)) #test mix
        self.assertEqual(1, addList(1))
        self.assertEqual((4, 'We removed your strings'), addList(1, 'a',3))#test list with string
        self.assertEqual("No numbers in string, please try again", addList('b', 'a'))#test list with all strings
    def testCosList(self):
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,1,-1], cosList(90,0,180))
        
    
    def testCubeList(self):
        self.assertEqual([1,8,27], cubeList(1,2,3))
        self.assertEqual([-1,-8,-27], cubeList(-1,-2,-3))
    def testCuberootList(self):
        self.assertEqual(([1.0, 2.0], [-1.0]), cuberootList(-1,1,8))
        
    def testDivideLists(self):
        self.assertEqual([2,2], divideLists([4,2], [2,1]))
        self.assertEqual("Inputs not of same length, please try again", divideLists([1], [1,2]))
        
    def testFactorialList(self):
        self.assertEqual([1,2,6], factorialList(1,2,3))
        
    def testMultiplyList(self):
        self.assertEqual(6, multiplyList(1,2,3))
        self.assertEqual(-6, multiplyList(-1,-2,-3))
    def testReciprocalList(self):
        self.assertEqual([1,0.5, 0.25], reciprocalList(1,2,4))
        self.assertEqual([-1,-0.5, -1/3], reciprocalList(-1,-2,-3))
    def testSquareList(self):
        self.assertEqual([1,4, 9], squareList(1,2,3))
        self.assertEqual([1,4, 9], squareList(-1,-2,-3))
        
    def testSineList(self):
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([1,0,0], sineList(90,0,180))
        
    def testSquareGenerator(self):
        #set up the generator with some inputs
        square = squareGenerator(1,2,3)
        #test that each iteration works
        self.assertEqual(1, next(square))
        self.assertEqual(4, next(square))
        self.assertEqual(9, next(square))
        
    def testSquarerootList(self):
        self.assertEqual([1,2, 3], squarerootList(1,4,9))
        self.assertEqual([1,2, 3], squarerootList(-1,1,4,9)) 
    def testSubtractLists(self):
        self.assertEqual([1,1], subtractLists([2,2], [1,1]))
    def testTanList(self):
        #the assertAlmostEqual function doesn't work here as it cannot subtract lists pairwise.
        #imported numpy and used it's testing function. This returns error in unittest if the numpy test breaks
        
        np.testing.assert_almost_equal([0,0], tangentList(0,180))
#        np.testing.assert_almost_equal([0, tangent(0))
#        self.assertAlmostEqual(0, tangent(180))
#        self.assertAlmostEqual(0, tangent(-180))
#        self.assertEqual("Strings not allowed, please try again", tangent("90"))
        
if __name__ == '__main__':        
    unittest.main()