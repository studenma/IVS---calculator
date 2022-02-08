class Maths:

	ans = 0 

	def add(self, numbers):
		result = 0
		for number in numbers:
			result += number
		self.ans = result

	def substract(self, numbers):
		result = numbers[0]
		iternum = iter(numbers)
		next(iternum)
		for number in iternum: 
			result -= number
		self.ans = result

	def mult(self, numbers):
		result = numbers[0]
		iternum = iter(numbers)
		next(iternum)
		for number in iternum: 
			result *= number
		self.ans = result

	def div(self, dividend, factor):
		if dividend == factor:
			self.ans = 1
			return
		if factor == 0:
			self.ans = None
			return
		self.ans = dividend/factor

	def modulo(self, dividend, factor):
		if factor == 0:
			self.ans = None
			return
		self.ans = dividend % factor

	def pow(self, number, exponent):
		result = number
		if exponent == 0:
			self.ans = 1
			return
		if exponent > 15:
			self.ans = None
			return
		for i in range(1, abs(exponent)):
			result *= number
		if exponent < 0:
			self.ans = 1.0/result
			return
		self.ans = result

	def factorial(self, number):
		result = 1
		if isinstance(number, float):
			self.ans = None
			return
		if number == 0:
			self.ans = result
			return
		if number < 0:
			self.ans = None
			return
		if number > 10:
			self.ans = None
			return
		for i in range(1, number+1):
			result *= i
		self.ans = result