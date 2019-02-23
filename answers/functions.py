import re

def add():
	print('type a number')
	left = input()
	if not re.match('\d+', left):
		raise TypeError('expected a digit')

	print('type another number')
	right = input()
	if not re.match('\d+', right):
		raise TypeError('expected a digit')
	return int(left) + int(right)

def subtract():
	print('type a number')
	left = int(input())

	print('type another number')
	right = int(input())
	return left - right

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
