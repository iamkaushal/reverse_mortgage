from django.db import models


class MortgageCalculation(models.Model):
    age = models.PositiveIntegerField()
    home_value = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_principal_limit(self, margin):
        # This is a placeholder for the actual principal limit calculation
        # Replace this with the correct formula
        return self.home_value * (1 + margin / 100) * (self.age / 100)
