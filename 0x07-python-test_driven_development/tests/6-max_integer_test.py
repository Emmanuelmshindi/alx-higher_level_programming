#!/usr/bin/python3
""" Unittests for max_integer[(...)] """

import unittest
max_integer = __import__('6-max_integer').max_integer




class TestMaxInteger(unittest.TestCase):
    """ Define unit tests for max_integer([...])."""

    def test_ordered_list(self):
        """ Define unit test for an ordered list """
        odered = [1, 2, 3, 4]
        self.assertEqual(max_integer(odered), 4)

    def test_unodered_list(self):
        """ Define unit test fro an unodered list """
        unodered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unodered), 4)

    def test_empty_list(self):
        """ Define unit test fro an empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_beginning(self):
        """ Test a list with a beginning max value """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_element_list(self):
        """ Test a list with one element """
        one_element_list = [4]
        self.asserEqual(max_integer(one_element_list), 4)

    def test_floats(self):
        """ Define unit test for a list with floats """
        list_with_floats = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(max_integer(list_with_floats), 4.5)

    def test_ints_and_floats(self):
        """ Define unit test for a list with ints and floats """
        list_with_ints_and_floats = [1.53, 3.5, 5, 10, 15.5]
        self.assertEqual(max_integer(list_with_ints_and_floats), 15.5)

    def test_string(self):
        """ Define unit test for a string """
        string = "Brennan"
        self.assertEqual(max_integer(string), r)

    def test_list_of_strings(self):
        """ Define unit test for a list of strings """
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """ Define unit test for an emty string """
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
