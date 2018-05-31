from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .forms import PersonForm
from .models import Person


# def persons_list(request):
#     persons = Person.objects.all()
#     return render(request, 'person_list.html', {'persons': persons})


class PersonList(ListView):
    """
    Uma ListView trabalha para listar coisas, como podemos ver, ao atrelar ela a um Model (Person, por exemplo)
    ele automaticamente retorna as instâncias gravadas, chama um template padrão (ex: person_list.html)
    passando a variável object_list onde está o iterável com as instâncias do banco.
    """
    model = Person


@method_decorator(login_required, name='dispatch')
class PersonDetail(DetailView):
    """
    Este tipo de view (DetailView) se atrela ao objeto para buscar informações de um objeto específico,
    dentro do template ele irá injetar um object com as informações do cliente.
    """
    model = Person


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})
