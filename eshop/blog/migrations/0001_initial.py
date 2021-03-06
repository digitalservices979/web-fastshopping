# Generated by Django 2.2.4 on 2019-09-11 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
