from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from . import views


urlpatterns = [
    path(
        'topping/list/',
        views.ToppingListAPIView.as_view(),
        name='topping-list',
    ),
    path(
        'food/list/',
        views.FoodListAPIView.as_view(),
        name='food-list',
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
]
