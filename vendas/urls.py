from django.urls import path

from vendas.views import DashboardView, NovoPedido, NovoItemPedido, ListaVendas

urlpatterns = [
    path('', ListaVendas.as_view(), name="lista-vendas"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('novo-pedido', NovoPedido.as_view(), name="novo-pedido"),
    path('novo-item-pedido/<int:venda>', NovoItemPedido.as_view(), name="novo-item-pedido"),
]
