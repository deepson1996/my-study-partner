from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request): # for one page as homepage
    return HttpResponse('Hello World!')

def room(request):
    return HttpResponse('Hello Room!') # another page in /room
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room),
]
