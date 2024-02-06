# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:25:19 2024

@author: chillale sai krishna
"""

# Unittesting 

import unittest
from divisible import div
from Interleave import inter_string


class TestDivisible(unittest.TestCase):


    def test_divisible_by_5_and_7(self):
        # Test if the function returns numbers divisible by both 5 and 7
        result = list(div(100))
        expected_result = [0, 35, 70]
        self.assertEqual(result, expected_result)

    def test_negative_input(self):
        # Test if the function handles negative input correctly
        result = list(div(-20))
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_zero_input(self):
        # Test if the function handles zero input correctly
        result = list(div(0))
        expected_result = [0]
        self.assertEqual(result, expected_result)
        
        
class TestInterleaveStrings(unittest.TestCase):

    def test_interleave_equal_length_strings(self):
        # Test if the function correctly interleaves two strings of equal length
        result = list(inter_string("abc", "123"))
        expected_result = ["a", "1", "b", "2", "c", "3"]
        self.assertEqual(result, expected_result)

    def test_interleave_different_length_strings_1(self):
        # Test if the function correctly interleaves two strings with string_1 longer than string_2
        result = list(inter_string("abcdef", "123"))
        expected_result = ["a", "1", "b", "2", "c", "3", "d", "e", "f"]
        self.assertEqual(result, expected_result)

    def test_interleave_different_length_strings_2(self):
        # Test if the function correctly interleaves two strings with string_2 longer than string_1
        result = list(inter_string("abc", "123456"))
        expected_result = ["a", "1", "b", "2", "c", "3", "4", "5", "6"]
        self.assertEqual(result, expected_result)

    def test_interleave_empty_string(self):
        # Test if the function handles empty strings correctly
        result = list(inter_string("", ""))
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_interleave_empty_string_with_nonempty_string(self):
        # Test if the function handles cases where one string is empty
        result = list(inter_string("", "abc"))
        expected_result = ["a", "b", "c"]
        self.assertEqual(result, expected_result)

    def test_interleave_nonempty_string_with_empty_string(self):
        # Test if the function handles cases where one string is empty
        result = list(inter_string("abc", ""))
        expected_result = ["a", "b", "c"]
        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
