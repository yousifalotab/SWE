from django.db import models
from django.contrib.auth.models import User

 
class Event(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    creationDate = models.DateTimeField(auto_now_add=True)
    
    def get_Name(self):
    return self.name
    
    def get_ID(self):
    return self.id
    
    def get_Description(self):
    return self.description
    
    def get_Creation_Date(self):
    return self


class Group(Event):
    idCounter = models.IntegerField()

class Meeting(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    id = models.TextField(max_length=30)
    idCounter = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(Member, models.CASCADE)
    group = models.ForeignKey(Group, models.CASCADE, related_name='meetings')
    
    def __init__(self, creator, group, name, description, date, time):
    self.idCounter+=1
    self.id = id
    self.creator = creator
    self.group = group
    self.name = name
    self.description = description
    self.date = date
    self.time = time
    
    def edit(self, name, description, date, time):
    self.name = name
    self.description = description
    self.date = date
    self.time = time
    
    def get_Name(self):
    return self.name
    
    def get_ID(self):
    return self.id
    



class OnlineCourse(Event):
    idCounter = models.IntegerField()