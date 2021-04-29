from django.urls import path
from . import views
urlpatterns = [
    #index
    path('', views.index, name='index'),
    #writer dashboard
    path('writer/', views.writer_view, name="writer_view"),
    #requester dashboard - not displaying db info
    path('requester/', views.requester_view, name="requester_view"),
    #request form
    path('submitRequest/', views.view_enter_request, name='requesting'),
    #not sure what this ones for
    path('request/', views.writer_req, name="writer_req"),
    #path('save/', views.view_save_request, name='save'),
    #writer view for particular request
    #path('writer_rev/', views.writer_review, name="writer_review"),
    #requester dashboard - duplicate? displays db data
  path('req_view/', views.requester_review, name="requester_view"),
    #requester page - writer view
  path('req_page', views.requester_view_particular_request, name="request_page"),
]


