import factory
from factory.django import DjangoModelFactory

from faker_food import FoodProvider

from .models import FoodCategory, Topping, Food


factory.Faker.add_provider(FoodProvider)


class FoodCategoryFactory(DjangoModelFactory):
    name = factory.Faker('ethnic_category')

    class Meta:
        model = FoodCategory


class ToppingFactory(DjangoModelFactory):
    name = factory.Faker('spice')

    class Meta:
        model = Topping


class FoodFactory(DjangoModelFactory):
    name = factory.Faker('dish')
    description = factory.Faker('dish_description')
    price = factory.Faker('pydecimal', min_value=10, max_value=2000)
    is_special = factory.Faker('pybool')
    is_vegan = factory.Faker('pybool')
    is_publish = factory.Faker('pybool')

    class Meta:
        model = Food
