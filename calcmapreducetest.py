# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:52:42 2018

@author: Martin PC

"""

import unittest
from calcmapreduce import addList, cosList, cubeList, divideLists, multiplyList, reciprocalList, squareList, squareGenerator, squarerootList, subtractLists

class CalcmapreduceTest(unittest.TestCase): #inherits from unittest
    
    def testAddList(self):
        #fn to test add fn
        self.assertEqual(10, addList(1,2,3,4)) #test + numbers
        self.assertEqual(-10, addList(-1,-2,-3, -4)) #test - numbers
        self.assertEqual(2, addList(1,-2,3)) #test mix
        self.assertEqual(1, addList(1)) #test one number
        
#    def testCosList(self):
#        self.assertAlmostEqual([0,1,-1], cubeList(90,0,180))
        
    def testDivideLists(self):
        self.assertEqual([2,2], divideLists([4,2], [2,1]))
    def testCubeList(self):
        self.assertEqual([1,8,27], cubeList(1,2,3))
        self.assertEqual([-1,-8,-27], cubeList(-1,-2,-3))
    def testMultiplyList(self):
        self.assertEqual(6, multiplyList(1,2,3))
        self.assertEqual(-6, multiplyList(-1,-2,-3))
    def testReciprocalList(self):
        self.assertEqual([1,0.5, 0.25], reciprocalList(1,2,4))
        self.assertEqual([-1,-0.5, -1/3], reciprocalList(-1,-2,-3))
    def testSquareList(self):
        self.assertEqual([1,4, 9], squareList(1,2,3))
        self.assertEqual([1,4, 9], squareList(-1,-2,-3))
#    def testSquareGenerator(self):
#        self.squareGenerator([1,2,3])
#        self.assertEqual(1, next(sq))
    def testSquarerootList(self):
        self.assertEqual([1,2, 3], squarerootList(1,4,9))
        self.assertEqual([1,2, 3], squarerootList(-1,1,4,9)) 
    def testSubtractLists(self):
        self.assertEqual([1,1], subtractLists([2,2], [1,1]))
        
if __name__ == '__main__':        
    unittest.main()