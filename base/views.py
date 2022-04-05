from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]
# Create your views here.
def home(request): # for one page as homepage
    rooms = Room.objects.all() # overrites rooms
    context = {"rooms": rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    #getting from database
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)