from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Event, EventData
from rest_framework import generics,response,status
from .forms import EventForm, EventDataForm

class SauronEyeAPI(generics.GenericAPIView):

    def post(self, request):
        data = request.data

        if request.method == "POST":

            form1 = EventForm(data)
            # return response.Response('success',status=200)

            if form1.is_valid():

                event = form1.save(commit=False)
                event.save()
                
                print(event.id)
                form2 = EventDataForm(data['data'])

                if form2.is_valid():
                    eventdata = form2.save(commit=False)
                    eventdata.session = event
                    print('true4')

                    event.save()
                    eventdata.save()


        return response.Response('success',status=200)


