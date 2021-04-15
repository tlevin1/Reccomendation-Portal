from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="Authentication/index.html")),
    path('authLogOut/', views.logoff, name="logoff"),
    path('accounts/', include('allauth.urls')),
]
