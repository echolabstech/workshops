from functions import add, subtract, multiply, divide

class Calculator():
	def run(self, operator=None, left=None, right=None):
		operator = operator or input()
		if operator == 'a':
			result = add(left, right)
		elif operator == 's':
			result = subtract()
		elif operator == 'm':
			result = multiply()
		elif operator == 'd':
			result = divide()
		return result