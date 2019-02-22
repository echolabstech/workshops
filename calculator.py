from functions import add, subtract, multiply, divide

print('operations are: a(add), s(subtract), m(multiply), d(divide)')
operator = input()
if operator == 'a':
	add()
elif operator == 's':
	subtract()
elif operator == 'm':
	multiply()
elif operator == 'd':
	divide()