from django.urls import path
from django.views.generic.base import TemplateView
from .views import home, my_logout, ContactTemplateView, PudimView

urlpatterns = [
    path('', home, name="home"),
    path('about/', TemplateView.as_view(template_name='about.html'), name="about"), # TemplateView, permite direcionar para um HTML
    path('contact/', ContactTemplateView.as_view(), name="contact"), # View customizada, herda de TemplateView
    path('pudim/', PudimView.as_view(), name='pudim'),
    path('logout/', my_logout, name="logout"),
]