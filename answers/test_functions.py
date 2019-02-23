from unittest import TestCase
from unittest.mock import patch as mock
from functions import add
import random

class TestsAdd(TestCase):
	def setUp(self):
		self.input_value = '1'

	@mock('builtins.input')
	def test_add_returns_a_number(self, mock_input):
		mock_input.return_value = self.input_value
		result = add()
		self.assertEqual(type(result), int)

	@mock('builtins.input')
	def test_add_returns_a_sum(self, mock_input):
		mock_input.return_value = self.input_value
		result = add()
		self.assertEqual(result, 2)

	@mock('builtins.input')
	def test_add_raise_if_non_numbers(self, mock_input):
		mock_input.return_value = 'foobar'
		with self.assertRaises(TypeError):
			result = add()
