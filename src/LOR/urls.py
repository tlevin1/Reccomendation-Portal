from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('writer_rev/', views.writer_review, name="writer_review"),
]