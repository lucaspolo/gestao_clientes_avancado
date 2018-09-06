from django.urls import path

from produtos.views import api

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('person_list')), name="root"),
    # path('list/', PersonList.as_view(), name="person_list"),
    # path('rich_list/', RichPeopleList.as_view(), name="rich_list"),
    # path('detail/<int:pk>', PersonDetail.as_view(), name="person_detail"),
    # path('new/', PersonCreate.as_view(), name="person_new"),
    # path('update/<int:pk>/', PersonUpdate.as_view(), name="persons_update"),
    # path('delete/<int:pk>/', PersonDelete.as_view(), name="persons_delete"),
    # path('produto_bulk/', ProdutoBulk.as_view(), name="produto_delete"),
    path('api/', api, name="api"),
]
