#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_max_integer(self):
        """Test for max_integer"""
        self.assertEqual(max_integer([32, -67, 19, 87]), 87)

    def test_empty_list(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test for negative number"""
        self.assertEqual(max_integer([-32, -44, -12, -7]), -7)

    def test_zero(self):
        """Test for zero"""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_numbers(self):
        """Test for float number"""
        self.assertEqual(max_integer([55.5, 71.2, 9.98, -101.2]), 71.2)

    def test_max_operated_integer(self):
        """Test for max operated integer"""
        self.assertEqual(max_integer([2, 2 * 2, 3, -1]), 4)

    def test_list_loop(self):
        """Test for list loop"""
        new_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer([i * 10 for i in new_list]), 100)

    def test_only_one_number(self):
        """Test for only one number"""
        self.assertEqual(max_integer([5]), 5)

    def test_string_in_list(self):
        """Test for string in a list"""
        with self.assertRaises(TypeError):
            max_integer([12, 8, '5'])

    def test_tuple_in_list(self):
        """Test for tuple in list"""
        with self.assertRaises(TypeError):
            max_integer([100, (200, 300)])

    def test_number(self):
        """Test for number"""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_dic_in_list(self):
        """Test for dictionary in a list"""
        with self.assertRaises(KeyError):
            max_integer({'size1': 5, 'size2': 10})
