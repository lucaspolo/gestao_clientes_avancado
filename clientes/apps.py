from decouple import config
from django.apps import AppConfig
from django.core.mail import mail_admins


class ClientesConfig(AppConfig):
    name = 'clientes'
