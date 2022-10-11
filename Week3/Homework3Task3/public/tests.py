#!/usr/bin/env python3
from unittest import TestCase

from public import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

class PublicTestSuite(TestCase):

    def test_case0(self):
        actual = script.rot_n()
        m = "The rot_n function should return a string!"
        self.assertTrue(isinstance(actual, str), m)

    def test_case1(self):
        script.plain_text = "abzAZ!"
        script.shift_by = 1
        res = script.rot_n()
        self.assertEqual(res, "bcaBA!")

    def test_case2(self):
        script.plain_text = "abzAZ!"
        script.shift_by = 0
        res = script.rot_n()
        self.assertEqual(res, "abzAZ!")

    def test_case3(self):
        script.plain_text = "ab#[z./0AZ!"
        script.shift_by = -10
        res = script.rot_n()
        self.assertEqual(res, "qr#[p./0QP!")

    def test_case4(self):
        script.plain_text = "...$%@#{[]ZAazyX"
        script.shift_by = 121
        res = script.rot_n()
        self.assertEqual(res, "...$%@#{[]QRrqpO")

    def test_case5(self):
        script.plain_text = ""
        script.shift_by = 121
        res = script.rot_n()
        self.assertEqual(res, "")
