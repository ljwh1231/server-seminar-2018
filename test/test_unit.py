import unittest

def f(items):
	value = 1
	for item in items:
		value *= item;
	return value

class MultiplyTestCase(unittest.TestCase):
	def test_multiply(self):
		self.assertEqual(6, f([1, 2, 3]))
		self.assertNotEqual(15, f([0, 3, 5]))
