from django.urls import path
from . import views

urlpatterns = [
        path('request_view/', views.request_view, name='request_view'),
]
