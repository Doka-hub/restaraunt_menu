from django.db.models import Prefetch

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)

from rest_framework.generics import ListAPIView

from .filters import filter_none_data_clear
from .serializers import (
    FoodCategoryListSerializer,
    ToppingSerializer,
    FoodFilterSerializer,
)
from .models import FoodCategory, Topping, Food


class ToppingListAPIView(ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    http_method_names = ['get']

    @extend_schema(
        description='List of toppings'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, *kwargs)


class FoodListAPIView(ListAPIView):
    queryset = FoodCategory.objects.filter(
        is_publish=True,
    ).order_by('id')
    serializer_class = FoodCategoryListSerializer

    http_method_names = ['get']

    def get_queryset(self):
        food_filter_serializer = FoodFilterSerializer(self.request.GET)
        queryset = self.queryset.prefetch_related(
            Prefetch(
                'foods',
                queryset=Food.objects.filter(
                    is_publish=True,
                    **filter_none_data_clear(food_filter_serializer.data)
                ),
            ),
        )
        return queryset

    @extend_schema(
        description='List of food',
        parameters=[
            OpenApiParameter(
                'is_special',
                bool,
                description='Filter by is_special',
            ),
            OpenApiParameter(
                'is_vegan',
                bool,
                description='Filter by is_vegan',
            ),
            OpenApiParameter(
                'toppings__name',
                str,
                description='Filter by topping name ',
                examples=[OpenApiExample('Paprika')]
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
