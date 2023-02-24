#!/usr/bin/env python3

from unittest import TestCase
from public.script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example0(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "Abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "Abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi Mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example2(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi 123mastarddsaf batch"
        actual = f.filter(msg)
        expected = "abc defghi 123?#$?#$?dsaf ?#$?#"
        self.assertEqual(expected, actual)
    
    def test_example3(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard", "hot"], "?#$")
        msg = "abc dshoti mastard jklmno"
        actual = f.filter(msg)
        expected = "abc d?#$?i ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
