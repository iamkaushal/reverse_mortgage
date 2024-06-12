from django import forms
from .models import MortgageCalculation


class MortgageCalculationForm(forms.ModelForm):
    margin = forms.ChoiceField(choices=[(i, f'{i}%') for i in range(1, 6)], label='Margin')

    class Meta:
        model = MortgageCalculation
        fields = ['age', 'home_value']
