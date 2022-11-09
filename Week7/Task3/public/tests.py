#!/usr/bin/env python3
from unittest import TestCase
from public.script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):
    
    def test_non_list(self):
        self.assertEqual("Invalid Input Type", max_profit(4))
    
    def test_empty_list(self):
        self.assertEqual("Empty Price List", max_profit([]))
    
    def test_non_int_el(self):
        self.assertEqual("Invalid Data Type within List", max_profit(["a", 'b']))
    
    def test_negative_el(self):
        self.assertEqual("Invalid Prices", max_profit([-10, 3, 5]),)
    
    def test_no_pair0(self):
        self.assertEqual(0, max_profit([3]))
    
    def test_no_pair1(self):
        self.assertEqual(0, max_profit([5, 5, 4, 3, 2, 1, 0]))
    
    def test_no_pair2(self):
        self.assertEqual(0, max_profit([2, 2]))
    
    def test_no_pair3(self):
        self.assertEqual(0, max_profit([5, 3, 3, 2, 2, 2, 0]))

    def test_correct0(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5]))
    
    def test_correct1(self):
        self.assertEqual(4, max_profit([6, 5, 3, 2, 1, 5]))
    
    def test_correct2(self):
        self.assertEqual(2, max_profit([1, 2, 2, 3, 3, 2, 2]))
    
    


#print(max_profit(4))
#print(max_profit([]))
#print(max_profit(["a", 'b']))
#print(max_profit([2.0, 3.0]))
#print(max_profit([-10, 3.0]))
#print(max_profit([5 ,4 , 3, 2, 1, 5]))

