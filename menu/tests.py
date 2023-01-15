from django.shortcuts import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from random import choice

from pprint import pprint

from .management.commands import test_data_create


class FoodTestCase(APITestCase):
    num_food_categories = 5
    num_toppings = 20
    num_foods = 200

    @classmethod
    def setUpTestData(cls):
        cls.test_data = test_data_create(
            cls.num_food_categories,
            cls.num_toppings,
            cls.num_foods,
        )

    def setUp(self):
        self.url = reverse('food-list')

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json['count'], self.num_food_categories)

        pprint(response_json, sort_dicts=False)


class ToppingTestCase(APITestCase):
    num_toppings = 20

    @classmethod
    def setUpTestData(cls):
        cls.test_data = test_data_create(
            num_food_categories=0,
            num_toppings=cls.num_toppings,
            num_foods=0,
        )

    def setUp(self):
        self.url = reverse('topping-list')

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json['count'], self.num_toppings)
        self.assertIn(
            {'name': choice(self.test_data['toppings']).name},
            response_json['results'],
        )
        pprint(response_json)
