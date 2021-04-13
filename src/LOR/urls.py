from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('writer/', views.writer_view, name="writer_view"),
    path('submitRequest/', views.view_enter_request, name='requesting'),
    path('request/', views.writer_req, name="writer_req"),
    #path('save/', views.view_save_request, name='save'),
path('writer_rev/', views.writer_review, name="writer_review"),
    path('uploadfile/',views.upload_file, name='upload_file'),
    path('uploadview/', views.upload_view, name='upload_view'),
    path('uploadview/<int:pk>/', views.delete_upload, name='delete_upload')
]
