from django.urls import path
from . import views

urlpatterns = [
    path('sauroneye/', views.sauroneye, name="sauroneye"),
]
