# Generated by Django 5.0.6 on 2024-06-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255)),
                ('userid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('ssl', models.BooleanField(default=False)),
            ],
        ),
    ]
