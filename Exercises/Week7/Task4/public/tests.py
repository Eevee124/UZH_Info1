#!/usr/bin/env python3
from unittest import TestCase
from public.script import evolve


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
class EvolveTestSuite(TestCase):

    def test_evolve1(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 4)
        expected = (
            (
                "--------------",
                "| ###        |",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEqual(expected, actual, f"Expected {expected} but instead {actual}")

        def test_evolve2(self):
            world = (
                "---",
                "|#|",
                "---"
            )
            actual = evolve(world, 2)
            expected = (
                (
                "---",
                "| |"
                "---"
            ),
            0
        )
        self.assertEqual(expected, actual, f"Expected {expected} but instead {actual}")

#INVALID INPUTS
    
    def test_invalid_tuple(self):
        self.assertRaises(Warning, evolve, list, 2)

    def test_invalid_char0(self):
        world = (
            "----------",
            "|     # 2|",
            "|   3 +  |",
            "|  #  #  |",
            "----------",
        )
        self.assertRaises(Warning, evolve, world, 2)

    def test_invalid_char1(self):
        world = (
            "|---|---|---|",
            "- |     #   -",
            "-    #  #  #-",
            "|    |  #    |",
            "-------------"
        )
        self.assertRaises(Warning, evolve, world, 3)

    def test_invalid_char2(self):
        world = (
            "-----------",
            " # # # # # ",
            "| ---    # |",
            "-----------|"
        )
        self.assertRaises(Warning, evolve, world, 5)

    def test_line_length(self):
        world = (
            "---------",
            "|         |",
            "|       |",
            "---------"
        )
        self.assertRaises(Warning, evolve, world, 3)
    
    def test_line_length1(self):
        world = (
            "-----",
            "|     |",
            "|     |",
            "-------"
        )
        self.assertRaises(Warning, evolve, world, 10)

    def test_size(self):
        world = (
            "--",
            "||"
            "||",
            "--"
        )
        self.assertRaises(Warning, evolve, world, 2)
    
    def test_size1(self):
        world = (
            "----",
            "----"
        )
        self.assertRaises(Warning, evolve, world, 1)

    def test_pos_int(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, -1)
    
    def test_pos_int1(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, 2.0)