from django.urls import path
from . import views

urlpatterns = [
    path('sauroneye/', views.SauronEyeAPI.as_view(), name="sauroneye"),
]
