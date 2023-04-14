# Generated by Django 4.2 on 2023-04-14 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=60, verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes', models.CharField(max_length=30, verbose_name='Type of clothes')),
                ('name_clothes', models.CharField(max_length=50, verbose_name='Full name of clothes')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='Photo')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'db_table': 'Product',
            },
        ),
    ]
