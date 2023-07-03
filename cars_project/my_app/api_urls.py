from . import api_views
from django.urls import path

urlpatterns = [
    path('contactus', api_views.serve_contactus),
    path('user', api_views.serve_person),
    path('car', api_views.serve_car)
]
