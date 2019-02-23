from unittest import TestCase
from unittest.mock import patch as mock, MagicMock
from app import some_workflow
from functions import add
from calculator import Calculator
import random

class TestsApp(TestCase):
	def setUp(self):
		pass

	def test_some_workflow_integration_test(self):
		pass
		## assert that all functions in the workflow
		## are called and passed expected arguments
		## BONUS check their return results
