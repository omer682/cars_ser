from . import api_views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('contactus', api_views.serve_contactus),
    path('user', api_views.serve_person),
    path('car', api_views.serve_car),
    path ('obtain-token', obtain_auth_token),
    path('logout', api_views.delete_token)
]
