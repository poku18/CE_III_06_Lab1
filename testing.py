import unittest
from lab1 import binarySearch, linearSearch

class SearchTestCase(unittest.TestCase):
	# Tests for binary search
	def testBinarySearch(self):
		values = [1, 2, 3 , 4, 5]
		self.assertEqual(binarySearch(values, 1), 0)
		self.assertEqual(binarySearch(values, 4), 3)
		self.assertEqual(binarySearch(values, 7), -1)
	# Tests for linear search
	def testLinearSearch(self):
		values = [1, 2, 3 , 4, 5]
		self.assertEqual(linearSearch(values, 1), 0)
		self.assertEqual(linearSearch(values, 4), 3)
		self.assertEqual(linearSearch(values, 7), -1)

if __name__ == '__main__':
	unittest.main()
