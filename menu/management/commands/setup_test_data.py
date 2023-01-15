# setup_test_data.py
from django.db import transaction
from django.core.management.base import BaseCommand

from random import choice, choices, randint

from menu.models import FoodCategory, Topping, Food
from menu.factories import (
    FoodCategoryFactory,
    ToppingFactory,
    FoodFactory,
)


def test_data_create(
        num_food_categories: int = 5,
        num_toppings: int = 20,
        num_foods: int = 200,
):
    food_categories = []
    for _ in range(num_food_categories):
        food_categories.append(FoodCategoryFactory())

    toppings = []
    for _ in range(num_toppings):
        toppings.append(ToppingFactory())

    foods = []
    for _ in range(num_foods):
        food = FoodFactory(category=choice(food_categories))
        food.toppings.add(*choices(toppings, k=randint(1, 5)))
        foods.append(food)

    return {
        'food_categories': food_categories,
        'toppings': toppings,
        'foods': foods,
    }


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [FoodCategory, Topping, Food]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        test_data_create()
