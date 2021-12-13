#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([32, -67, 19, 87]), 87)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-32, -44, -12, -7]), -7)

    def test_zero(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_numbers(self):
        self.assertEqual(max_integer([55.5, 71.2, 9.98, -101.2]), 71.2)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([2, 2 * 2, 3, -1]), 4)

    def test_list_loop(self):
        new_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer([i * 10 for i in new_list]), 100)

    def test_only_one_number(self):
        self.assertEqual(max_integer[5], 5)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([12, 8, '5'])

    def test_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([100, (200, 300)])

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_dic_in_list(self):
        with self.assertRaises(KeyError):
            max_integer({'size1': 5, 'size2': 10})
