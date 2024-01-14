from django.shortcuts import render

# Create your views here.

# cars/views.py

from django.shortcuts import render
from .forms import CarForm

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()

    return render(request, 'carsapp/templates/carsapp/car_form.html', {'form': form})
