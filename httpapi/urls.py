from django.urls import path,include
from . import views

urlpatterns = [
    path('switch/',views.switch,name="switch"),
]