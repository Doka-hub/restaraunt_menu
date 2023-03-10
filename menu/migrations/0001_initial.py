# Generated by Django 4.1.3 on 2023-01-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Публичный')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('is_special', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False, verbose_name='Вегетарианская')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Публичный')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='menu.foodcategory', verbose_name='Категория')),
                ('toppings', models.ManyToManyField(related_name='foods', to='menu.topping', verbose_name='Топинги')),
            ],
        ),
    ]
