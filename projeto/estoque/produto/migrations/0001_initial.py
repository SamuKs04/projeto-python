# Generated by Django 4.0.5 on 2022-06-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('código', models.CharField(max_length=30)),
                ('tamanho', models.CharField(max_length=100)),
            ],
        ),
    ]
