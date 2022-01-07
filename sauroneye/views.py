from django.shortcuts import render
from django.http import HttpResponse

from mordor.sauroneye.serializers import EventSerializer
from .models import Event, EventData
from rest_framework import generics,response,status

class SauronEyeAPI(generics.GenericAPIView):
    serialer_class = EventSerializer

    def post(self, request):

def sauroneye(request, pk):

    if request.method == "POST":



