# Generated by Django 2.0.1 on 2018-06-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20180624_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
