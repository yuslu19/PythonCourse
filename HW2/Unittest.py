# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:52:59 2020

@author: user
"""

import unittest
import LinearRegression

class RegressionTest(unittest.TestCase):
    
	def test_regression(self):                                                 #checks for a certain and simple x,y data set 
		self.assertEqual((0,[12.706204736432095, -12.706204736432095],1),LinearRegression.MyFun(np.array([1,0]),np.array([0,1])))
    def type_error(self):
        with self.assertRaises(TypeError):                                      #checks if the argument is a string
            LinearRegression.MyFun('b',5)
    def test_attribute(self):                                                   #checks if the argument is a np array
        with self.assertRasises(AttributeError):
            Linear.Regression.MyFun([1,2,3],[6,7,8])
    def test_dimension(self):                                                   #checks if the dimensions of the arguments match
        with self.assertRaises(Exception):
            Linear.Regression.MyFun(np.array([1,2,3]),np.array([6,7])
if __name__ == '__main__':
  unittest.main()