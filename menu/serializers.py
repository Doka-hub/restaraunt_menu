from rest_framework import serializers

from .filters import filter_none_data_clear, parse_query_parameters_list
from .models import FoodCategory, Topping, Food


class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = ['name']


class FoodFilterSerializer(serializers.Serializer):
    is_special = serializers.BooleanField(allow_null=True)
    is_vegan = serializers.BooleanField(allow_null=True)
    toppings__name = serializers.CharField(allow_null=True)

    def to_representation(self, instance):
        data = filter_none_data_clear(super().to_representation(instance))

        toppings__name = data.get('toppings__name')
        if toppings__name:
            data['toppings__name__in'] = parse_query_parameters_list(
                data['toppings__name']
            )
            del data['toppings__name']

        return data


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
