from django.db import models
import uuid

# Create your models here.
class Event(models.Model):
    # unique id key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    session_id = models.CharField(max_length=200)
    category = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(null=True)

class EventData(models.Model):
    session = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.CharField(max_length=500, null=False, blank=True)
    path = models.CharField(max_length=500, null=False, blank=True)