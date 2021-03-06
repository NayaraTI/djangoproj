# Generated by Django 4.0.4 on 2022-06-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(blank=True, max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mostrar', models.BooleanField(default=True)),
            ],
        ),
    ]
