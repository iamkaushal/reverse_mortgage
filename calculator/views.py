from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import MortgageCalculationForm


def calculate_mortgage(request):
    form = MortgageCalculationForm()
    return render(request, 'calculator/index.html', {'form': form})


@csrf_exempt
def calculate_principal_limit(request):
    age = int(request.GET.get('age', 0))
    home_value = float(request.GET.get('home_value', 0))
    margin = float(request.GET.get('margin', 0))

    principal_limit = home_value * (1 + margin / 100) * (age / 100)
    return JsonResponse({'principalLimit': principal_limit})
