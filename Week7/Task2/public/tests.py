#!/usr/bin/env python3
from unittest import TestCase
from public.script import convert_roman_to_int


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_basic(self, roman):
        actual = convert_roman_to_int(roman)
        m = "The function should return an int!"
        self.assertTrue(isinstance(actual, int), m)


    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)

    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    #def test_return_type(self):
    #    self.assertIsInstance(convert_roman_to_int(str), int)

    #Check that basic subtractive notation works correctly, e.g. "IV" is 4, "XL" is 40 and "CD" is 400, "IX" is 9, "XC" is 90 and "CM" is 900.

    def test_simple_sub1(self):
        self._assert("IV", 4)
    
    def test_simple_sub2(self):
        self._assert("XL", 40)
    
    def test_simple_sub3(self):
        self._assert("CD", 400)
    
    def test_simple_sub4(self):
        self._assert("IX", 9)

    def test_simple_sub5(self):
        self._assert("XC", 90)
    
    def test_simple_sub6(self):
        self._assert("CM", 900)
    
    def test_simple_longadd0(self):
        self._assert("VIII", 8)

    def test_simple_longadd1(self):
        self._assert("MDC", 1600)

    def test_simple_add_sub0(self):
        self._assert("XIV", 14)

    def test_simple_add_sub0(self):
        self._assert("XLI", 41)

#need to check that fct returns integer value
#need to check how raise Warning() works and implement this
#by rasising warning for:

# -numerals outside the valid roman numerals
# -
















