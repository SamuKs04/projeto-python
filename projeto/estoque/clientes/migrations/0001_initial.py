# Generated by Django 4.0.5 on 2022-06-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=13)),
                ('login', models.CharField(max_length=100)),
            ],
        ),
    ]
