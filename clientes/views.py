from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render_to_response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from produtos.models import Produto
from .models import Person


class PersonList(ListView):
    """
    Uma ListView trabalha para listar coisas, como podemos ver, ao atrelar ela a um Model (Person, por exemplo)
    ele automaticamente retorna as instâncias gravadas, chama um template padrão (ex: person_list.html)
    passando a variável object_list onde está o iterável com as instâncias do banco.
    """
    model = Person
    context_object_name = 'clientes'

    ordering = ['-salary']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        ja_acessou = self.request.session.get('ja_acessou')

        if not ja_acessou:
            context['message'] = 'Seja bem-vindo'
            self.request.session['ja_acessou'] = True
        else:
            context['message'] = 'Seja bem-vindo novamente'

        return context


class RichPeopleList(ListView):
    """
    Herdando de ListView e sobrescrevendo o método get_queryset com o filtro para pegar salarios maiores e iguais a 1000
    """
    template_name = 'clientes/person_list'
    context_object_name = "clientes"

    def get_queryset(self):
        return Person.objects.filter(salary__gte=1000).order_by('-salary')


class PersonDetail(DetailView):
    """
    Este tipo de view (DetailView) se atrela ao objeto para buscar informações de um objeto específico,
    dentro do template ele irá injetar um object com as informações do cliente.
    """
    model = Person
    context_object_name = 'cliente'


class PersonCreate(LoginRequiredMixin, CreateView):
    """
    Esta CBV permite gerenciar a criação de usuários, permitindo substituir, no atributo fields passamos os atributos
    do objeto que queremos no formulários, a success_url é onde irá caso esteja OK.
    """
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    """
    Similar ao CreateView, apenas implementamos o método get_success_url ao invés de definir success_url, assim temos
    mais controle no caso de sucesso.
    """
    model = Person
    template_name = 'clientes/person_form.html'
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    # success_url = reverse_lazy('person_list')

    def get_success_url(self):
        return reverse_lazy('person_list')


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')

# Criação de objetos no banco por Bulk Create


@method_decorator(login_required, name='dispatch')
class ProdutoBulk(View):

    def get(self, request):
        produtos = ['Banana', 'Maça', 'Limão', 'Laranja', 'Pera', 'Melancia']
        lista_produtos = []

        response = render_to_response('home.html')

        if not request.COOKIES.get('produto_bulk'):

            for produto in produtos:
                p = Produto(descricao=produto, preco=10)
                lista_produtos.append(p)

            Produto.objects.bulk_create(lista_produtos)

            response.set_cookie('produto_bulk', 'True', max_age=24*60*60)

        return response
