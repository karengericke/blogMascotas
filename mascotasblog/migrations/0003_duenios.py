# Generated by Django 3.2.9 on 2022-02-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotasblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duenios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('anios', models.IntegerField()),
            ],
        ),
    ]