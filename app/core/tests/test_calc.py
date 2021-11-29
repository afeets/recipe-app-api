from django.test import TestCase

""" add test case """
from core.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
