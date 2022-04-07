from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # Can be null blank is for save method and null is for database
    participants = models.ManyToManyField(User, related_name='parcitipants', blank=True)# stores all the users that are present in a room but before need to add participants
    updated = models.DateTimeField(auto_now=True) #updated at
    created = models.DateTimeField(auto_now_add=True) # created at

    class Meta:
        ordering = ['-updated', '-created']

    # String representation of room
    def __str__(self):
        return str(self.name)

#room has message
class Message(models.Model):
    # django already builts user model for default we use 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)# relationship when parent is deleted we can set this field to null by .SET_NULL, CASCADE->all data deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #updated at
    created = models.DateTimeField(auto_now_add=True) # created at
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.body[0:50])
