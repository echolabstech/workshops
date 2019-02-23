from calculator import Calculator

calc = Calculator()

def some_workflow():
	print('operations are: a(add), s(subtract), m(multiply), d(divide)')
	## the following line throws an error
	## TDD test and fix
	result = calc.run('a', '5', '3')
	print('the result is:' + str(result))
	return result

def other_work():
	pass

result = some_workflow()
