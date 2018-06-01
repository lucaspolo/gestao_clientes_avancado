from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Person


class PersonList(ListView):
    """
    Uma ListView trabalha para listar coisas, como podemos ver, ao atrelar ela a um Model (Person, por exemplo)
    ele automaticamente retorna as instâncias gravadas, chama um template padrão (ex: person_list.html)
    passando a variável object_list onde está o iterável com as instâncias do banco.
    """
    model = Person


class PersonDetail(DetailView):
    """
    Este tipo de view (DetailView) se atrela ao objeto para buscar informações de um objeto específico,
    dentro do template ele irá injetar um object com as informações do cliente.
    """
    model = Person


@method_decorator(login_required, name='dispatch')
class PersonCreate(CreateView):
    """
    Esta CBV permite gerenciar a criação de usuários, permitindo substituir, no atributo fields passamos os atributos
    do objeto que queremos no formulários, a success_url é onde irá caso esteja OK.
    """
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list')


@method_decorator(login_required, name='dispatch')
class PersonUpdate(UpdateView):
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


@method_decorator(login_required, name='dispatch')
class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')
