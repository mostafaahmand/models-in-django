from django.shortcuts import render
from .models import Place
# Create your views here.
def home(request):
    p = Place.objects.all()
    c = {'makan': p}
    return render (request ,'places/index.html', context=c)