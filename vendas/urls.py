from django.urls import path

from vendas.views import DashboardView, NovoPedido, NovoItemPedido, ListaVendas, EditPedido, DeletePedido

urlpatterns = [
    path('', ListaVendas.as_view(), name="lista-vendas"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('novo-pedido', NovoPedido.as_view(), name="novo-pedido"),
    path('edit-pedido/<int:venda>', EditPedido.as_view(), name="edit-item-pedido"),
    path('delete-pedido/<int:venda>', DeletePedido.as_view(), name="delete-pedido"),
    path('novo-item-pedido/<int:venda>', NovoItemPedido.as_view(), name="novo-item-pedido"),
]
