from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    is_publish = models.BooleanField(default=True, verbose_name='Публичный')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(
        FoodCategory,
        on_delete=models.CASCADE,
        related_name='foods',
        verbose_name='Категория',
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )

    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(
        default=False,
        verbose_name='Вегетарианская',
    )
    is_publish = models.BooleanField(default=True, verbose_name='Публичный')

    toppings = models.ManyToManyField(
        Topping,
        related_name='foods',
        blank=True,
        verbose_name='Топинги',
    )

    def __str__(self):
        return f'{self.category} | {self.name}'
