from django.urls import path
from . import views

urlpatterns = [
    path('submitRequest/', views.view_enter_request, name='requesting'),
    #path('save/', views.view_save_request, name='save'),
]