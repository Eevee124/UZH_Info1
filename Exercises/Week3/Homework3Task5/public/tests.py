#!/usr/bin/env python3
from unittest import TestCase
import math

from public import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".


class PublicTestSuite(TestCase):
    def test_return_type(self):
        actual = script.get_bmi_category()
        m = "The get_size function should return a string!"
        self.assertTrue(isinstance(actual, str), m)

    def test_case0(self):
        script.height = 1.75
        script.weight = 88
        res = script.get_bmi_category()
        self.assertEqual(res, "BMI: 28.73, Category: Pre-obesity")

    def test_case1(self):
        script.height = -10
        script.weight = -88
        res = script.get_bmi_category()
        self.assertEqual(res, "N/A")

    def test_case2(self):
        script.height = 10
        script.weight = 10
        res = script.get_bmi_category()
        self.assertEqual(res, "BMI: 0.10, Category: Underweight")
    
    def test_case3(self):
        script.height = -10
        script.weight = 1
        res = script.get_bmi_category()
        self.assertEqual(res, "N/A")
    
    def test_case4(self):
        script.height = 1.8
        script.weight = 59.95
        res = script.get_bmi_category()
        self.assertEqual(res, "BMI: 18.50, Category: Underweight")
    
    def test_case5(self):
        script.height = 1.8
        script.weight = 60
        res = script.get_bmi_category()
        self.assertEqual(res, "BMI: 18.52, Category: Normal weight")
    
    def test_case5(self):
        script.height = 0.000000000000001
        script.weight = 12345678900000000
        res = script.get_bmi_category()
        self.assertEqual(res, "BMI: 12345678899999998373956074294790837948796370944.00, Category: Obesity class III")