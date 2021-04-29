from django.urls import path
from . import views

urlpatterns = [
    path('writer-more-info/', views.writer_more_info, name='writer_more_info'),
path('view-more-info/', views.view_more_info, name='view_more_info'),
]
