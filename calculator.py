from functions import add, subtract, multiply, divide

class Calculator():
	def run(self):
		print('operations are: a(add), s(subtract), m(multiply), d(divide)')
		operator = input()
		if operator == 'a':
			result = add()
		elif operator == 's':
			result = subtract()
		elif operator == 'm':
			result = multiply()
		elif operator == 'd':
			result = divide()
		print('the result is:' + str(result))
