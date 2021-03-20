from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'home.html',{"images":images})