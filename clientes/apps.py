from decouple import config
from django.apps import AppConfig
from django.core.mail import mail_admins


class ClientesConfig(AppConfig):
    name = 'clientes'

    def ready(self):
        app_version = config('HEROKU_RELEASE_VERSION', default=None)

        if app_version:
            mail_admins(
                f'Aplicação iniciada {app_version}',
                f"A aplicação foi iniciada com sucesso, versao {app_version}",
                fail_silentyly=False,
            )
