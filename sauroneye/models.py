from django.db import models
import uuid

# Create your models here.
class Event(models.Model):
    # unique id key
    id = models.BigAutoField(unique=True, primary_key=True, editable=False)
    session_id = models.CharField(max_length=200)
    category = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(null=True)

    class Meta:
        ordering=('-timestamp',)
    
    def __str__(self):
        return self.session_id
    
class EventData(models.Model):
    session = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.CharField(max_length=500, null=False, blank=True)
    path = models.CharField(max_length=500, null=False, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.session