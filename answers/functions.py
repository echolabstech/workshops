import re

def add(left=None, right=None):
	print('type a number')
	left = left or input()
	if not re.match('\d+', left):
		raise TypeError('expected a digit')

	print('type another number')
	right = right or input()
	if not re.match('\d+', right):
		raise TypeError('expected a digit')
	return int(left) + int(right)

def subtract():
	"""
	implement using TDD
	"""
	pass

def multiply():
	"""
	implement using TDD
	"""
	pass

def divide():
	"""
	implement using TDD
	"""
	pass	
