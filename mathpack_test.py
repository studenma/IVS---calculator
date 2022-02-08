import unittest
from mathpack import Maths

mathclass = Maths()
numbers = []


class TestStringMethods(unittest.TestCase):

	def test_add(self):
		numbers = [2,2]
		mathclass.add(numbers)
		self.assertEqual(mathclass.ans, 4)
		numbers = [-2,2]
		mathclass.add(numbers)
		self.assertEqual(mathclass.ans, 0)
		numbers = [-2,-2]
		mathclass.add(numbers)
		self.assertEqual(mathclass.ans, -4)

	def test_substract(self):
		numbers = [2,2]
		mathclass.substract(numbers)
		self.assertEqual(mathclass.ans, 0)
		numbers = [-2,2]
		mathclass.substract(numbers)
		self.assertEqual(mathclass.ans, -4)
		numbers = [-2,-2]
		mathclass.substract(numbers)
		self.assertEqual(mathclass.ans, 0)

	def test_mult(self):
		numbers = [2,2]
		mathclass.mult(numbers)
		self.assertEqual(mathclass.ans, 4)
		numbers = [-2,2]
		mathclass.mult(numbers)
		self.assertEqual(mathclass.ans, -4)
		numbers = [-2,-2]
		mathclass.mult(numbers)
		self.assertEqual(mathclass.ans, 4)
		numbers = [0,-2]
		mathclass.mult(numbers)
		self.assertEqual(mathclass.ans, 0)

	def test_div(self):
		mathclass.div(2, 2)
		self.assertEqual(mathclass.ans, 1)
		mathclass.div(2, 1)
		self.assertEqual(mathclass.ans, 2)
		mathclass.div(2, 0)
		self.assertEqual(mathclass.ans, None)
		mathclass.div(0, 2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.div(6, -2)
		self.assertEqual(mathclass.ans, -3)
		mathclass.div(-6, 2)
		self.assertEqual(mathclass.ans, -3)
		mathclass.div(1,2)
		self.assertEqual(mathclass.ans, 0.5)
		mathclass.div(1.0,2)
		self.assertEqual(mathclass.ans, 0.5)

	def test_modulo(self):
		mathclass.modulo(2, 2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.modulo(2, 1)
		self.assertEqual(mathclass.ans, 0)
		mathclass.modulo(2, 0)
		self.assertEqual(mathclass.ans, None)
		mathclass.modulo(0, 2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.modulo(6, -2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.modulo(-6, 2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.modulo(1,2)
		self.assertEqual(mathclass.ans, 1)
		mathclass.modulo(1.0,2)
		self.assertEqual(mathclass.ans, 1)
		mathclass.modulo(0.5,0.75)
		self.assertEqual(mathclass.ans, 0.5)

	def test_pow(self):
		mathclass.pow(2, 2)
		self.assertEqual(mathclass.ans, 4)
		mathclass.pow(2, 1)
		self.assertEqual(mathclass.ans, 2)
		mathclass.pow(2, 0)
		self.assertEqual(mathclass.ans, 1)
		mathclass.pow(0, 2)
		self.assertEqual(mathclass.ans, 0)
		mathclass.pow(6, -2)
		self.assertEqual(mathclass.ans, 1.0/36)
		mathclass.pow(-6, 2)
		self.assertEqual(mathclass.ans, 36)
		mathclass.pow(1,2)
		self.assertEqual(mathclass.ans, 1)

	def test_factorial(self):
		mathclass.factorial(2)
		self.assertEqual(mathclass.ans, 2)
		mathclass.factorial(5)
		self.assertEqual(mathclass.ans, 120)
		mathclass.factorial(11)
		self.assertEqual(mathclass.ans, None)
		mathclass.factorial(-1)
		self.assertEqual(mathclass.ans, None)
		mathclass.factorial(0)
		self.assertEqual(mathclass.ans, 1)
		mathclass.factorial(1.5)
		self.assertEqual(mathclass.ans, None)

if __name__ == '__main__':
    unittest.main()