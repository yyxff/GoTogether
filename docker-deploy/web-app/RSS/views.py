from django.shortcuts import render
from user.models import CarModel
def index_view(request):
    if request.user.is_authenticated:
        cars = CarModel.objects.filter(user=request.user)
        context = {'cars': cars}
        return render(request, 'base.html', context=context)
    return render(request, 'base.html')