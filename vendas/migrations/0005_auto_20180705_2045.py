# Generated by Django 2.0.1 on 2018-07-05 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20180624_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar parâmetro NF-e'), ('permissao2', 'Permissao 2'), ('permissao3', 'Permissao 3'))},
        ),
    ]
