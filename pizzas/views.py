from django.shortcuts import render

from .models import Pizza, Topping

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')