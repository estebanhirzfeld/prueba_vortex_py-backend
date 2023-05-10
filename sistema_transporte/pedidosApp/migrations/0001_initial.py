# Generated by Django 4.2 on 2023-05-10 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conductoresApp', '0008_alter_conductor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('tipo_pedido', models.CharField(max_length=20, verbose_name='Tipo')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('conductor_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='conductoresApp.conductor')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]