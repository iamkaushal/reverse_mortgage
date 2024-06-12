from django.test import TestCase
from .models import MortgageCalculation


class MortgageCalculationTest(TestCase):

    def test_calculate_principal_limit(self):
        calc = MortgageCalculation(age=70, home_value=300000)
        principal_limit = calc.calculate_principal_limit(3)
        self.assertAlmostEqual(principal_limit, 216300, places=2)
