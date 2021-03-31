from django.urls import path
from . import views

urlpatterns = [
    path('', views.writer_review, name='review'),
    path('writerrev/', views.writer_review, name="writer_review"),
]
