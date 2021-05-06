from django.urls import path
from . import views

urlpatterns = [
    path('uploadfile/', views.upload_file, name='upload_file'),
    path('uploadview/', views.upload_view, name='upload_view'),
    path('uploadview2/', views.upload_view2, name='upload_view2'),
    path('uploadview/<int:pk>/', views.delete_upload, name='delete_upload')
]
