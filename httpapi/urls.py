from django.urls import path,include
from . import views

urlpatterns = [
    path('switch/',views.switch,name="switch"),
    path('get_status/',views.get_status,name="get_status"),
]