from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from produtos.models import Produto


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)


    @property
    def nome_completo(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ctx = {
            'cliente': self,
        }

        plain_message = render_to_string('clientes/emails/novo_usuario.txt', ctx)
        html_message = render_to_string("clientes/emails/novo_usuario.html", ctx)

        send_mail(
            'Nova cliente cadastrado!',
            plain_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            html_message=html_message,
        )
