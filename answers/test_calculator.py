from unittest import TestCase
from unittest.mock import patch as mock, MagicMock
from app import some_workflow
from functions import add
from calculator import Calculator
import random

class TestsApp(TestCase):
	def setUp(self):
		self.mock_add = MagicMock(add)

	@mock('calculator.Calculator.run')
	@mock('builtins.input')
	def test_some_workflow_integration_test(self, mock_input, mock_run):
		mock_run.return_value = 8
		result = some_workflow()
		self.assertEqual(result, 8)
		self.assertFalse(mock_input.called)
		self.assertTrue(mock_run.called)
		self.assertEqual(mock_run.call_args[0], ('a', '5', '3'))
