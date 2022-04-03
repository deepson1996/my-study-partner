from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request): # for one page as homepage
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')