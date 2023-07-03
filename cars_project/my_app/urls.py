from . import views
from django.urls import path


urlpatterns =  [
    path("base", views.serve_base, name='base'),
    path('cars', views.serve_cars, name="cars"),
    path('car/id', views.serve_car_id, name="carid"),
    path('search', views.serve_search_bar),
    path("contact", views.serve_contact),
    path('car/add', views.add_car),
    path('', views.serve_base),
    path('car/update/<int:car_id>', views.update_car, name='update_cars'),
    path('cars_own', views.owner_cars, name = 'cars_own'),
    path('testupdate/<int:car_id>', views.test_update),
    path("login", views.serve_login),
    path('signup', views.signup),
    path('test', views.testing),
    path('logout/', views.site_logout, name='logout')
]