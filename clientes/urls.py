from django.urls import path

from .views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete
from .views import ProdutoBulk

urlpatterns = [
    path('list/', PersonList.as_view(), name="person_list"),
    path('detail/<int:pk>', PersonDetail.as_view(), name="person_detail"),
    path('new/', PersonCreate.as_view(), name="person_new"),
    path('update/<int:pk>/', PersonUpdate.as_view(), name="persons_update"),
    path('delete/<int:pk>/', PersonDelete.as_view(), name="persons_delete"),
    path('produto_bulk/', ProdutoBulk.as_view(), name="produto_delete"),
]