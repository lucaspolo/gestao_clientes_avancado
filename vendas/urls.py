from django.urls import path

from vendas.views import DashboardView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="dashboard"),
]
