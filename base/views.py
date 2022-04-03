from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request): # for one page as homepage
    return HttpResponse('Hello World!')

def room(request):
    return HttpResponse('Hello Room!') # another page in /room