from django.contrib import admin
from .models import Event,EventData

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=['id','name','session_id','timestamp','category']
    search_fields=['timestamp','session_id','name']
    list_per_page=5

class EventDataAdmin(admin.ModelAdmin):
    list_display=['host','session']
    search_fields=['host','session']
    list_per_page=5

admin.site.register(Event,EventAdmin)
admin.site.register(EventData,EventDataAdmin)