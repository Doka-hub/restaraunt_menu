from rest_framework import serializers

from .models import FoodCategory, Topping, Food


class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = ['name']


class FoodFilterSerializer(serializers.Serializer):
    is_special = serializers.BooleanField(allow_null=True)
    is_vegan = serializers.BooleanField(allow_null=True)
    toppings__name = serializers.CharField(allow_null=True)


class FoodListSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Food
        fields = [
            'id',

            'name',
            'description',
            'price',

            'is_special',
            'is_vegan',
            'is_publish',

            'toppings',
        ]


class FoodCategoryListSerializer(serializers.ModelSerializer):
    foods = FoodListSerializer(many=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'is_publish', 'foods']
