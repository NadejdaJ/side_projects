''' Need to write unit tests for the following problem:

Fizzbuzz:

Write a program that prints the numbers from 1 to 100. But

-- for multiples of three print "Fizz" instead of the number
-- for the multiples of five print "Buzz".
-- for numbers which are multiples of both three and five print "FizzBuzz".

Hence:

Test 1: is the total numbers in the output 100?
Test 2: are they printed out in the correct sequence?
Test 3: if 'Fizz' is found then is the corresponding number divisible by 3?
Test 4: if 'Buzz' is found then is the corresponding number divisible by 5?
Test 5: if 'FizzBuzz' is found then is the corresponding number divisible by both 3 and 5?
'''

import unittest
from fizzbuzz import *


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_divisible3(self):
        self.assertEqual(divisible3(3), True)
        self.assertEqual(divisible3(5), False)

    def test_divisible5(self):
        self.assertEqual(divisible5(5), True)
        self.assertEqual(divisible5(3), False)

    def test_divisible35(self):
        self.assertEqual(divisible35(15), True)
        self.assertEqual(divisible35(10), False)

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz([1, 2, 7, 41]), [1, 2, 7, 41])
        self.assertEqual(fizzbuzz([3, 12]), ['Fizz', 'Fizz'])
        self.assertEqual(fizzbuzz([10, 25]), ['Buzz', 'Buzz'])
        self.assertEqual(fizzbuzz([30, 60]), ['FizzBuzz', 'FizzBuzz'])


if __name__ == '__main__':
    unittest.main()
