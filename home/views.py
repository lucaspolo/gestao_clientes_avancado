from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, View


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class ContactTemplateView(TemplateView):
    """
    A TemplateView facilita a criação de views que apenas chamam as templates ou é baseada em uma template.
    """
    template_name = 'contact.html'


class PudimView(View):
    """
    A basic View permite que você implemente métodos por método HTTP, facilitando muito o controle.
    """

    def get(self, request, *args, **kwargs):
        return render(request,'pudim.html')