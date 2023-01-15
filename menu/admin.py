from django.contrib import admin

from .models import FoodCategory, Topping, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'is_publish',
    ]


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category',

        'name',
        'price',

        'is_special',
        'is_vegan',
        'is_publish',
    ]
