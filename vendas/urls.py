from django.urls import path

from vendas.views import DashboardView, NovoPedido

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="novo-pedido"),
    path('novo-pedido', NovoPedido.as_view(), name="dashboard"),
]
