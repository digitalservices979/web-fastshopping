# Generated by Django 2.2.3 on 2019-07-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20190719_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_product2',
            field=models.ImageField(height_field='height', upload_to='products', verbose_name='Primera Imagen', width_field='width'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_product3',
            field=models.ImageField(height_field='height', upload_to='products', verbose_name='Segunda Imagen', width_field='width'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_product4',
            field=models.ImageField(height_field='height', upload_to='products', verbose_name='Tercera Imagen', width_field='width'),
        ),
    ]
