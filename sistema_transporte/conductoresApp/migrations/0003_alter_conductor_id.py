# Generated by Django 4.2 on 2023-04-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conductoresApp', '0002_rename_identificaion_conductor_identicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='id',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]