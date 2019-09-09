from django.urls import path

from products import views

urlpatterns = [

    path('index/', views.index),
    path('', views.home),
    path('academics/', views.academics),
    path('cultureandarts/', views.culture),
    path('feedingprogram/', views.feedingprogram),
    path('donate/', views.donate),
    path('notification/', views.notifications)
]
