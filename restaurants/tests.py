# from django.test import TestCase
from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import RestaurantModel, User, MenuModel, EmployeeModel


class TestRestaurants(APITestCase):
    """Class --- test"""

    def setUp(self):
        self.user = User.objects.create_user(username="mimmm", password="root")
        self.user.is_staff = True
        self.user.save()

        EmployeeModel.objects.create(user=self.user,
                                     position="It manager")

        restaurant = RestaurantModel.objects.create(name="Flat 56",
                                                    rating=94,
                                                    contact_no="0676767674",
                                                    address="Zelena 45"
                                                    )
        RestaurantModel.objects.create(name="Green Lion",
                                       rating=88,
                                       contact_no="0989090004",
                                       address="Shevchenka 77"
                                       )
        MenuModel.objects.create(restaurant=restaurant,
                                 menu="a kind of menu")

    def test_display_restaurant_list_view(self):
        response = self.client.get(reverse("restaurants"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_upload_menu(self):
        expected = {'message': 'Menu Created Succesfully',
                    'data': {'id': 4, 'date': '2022-09-16', 'menu': 'menu menu menu', 'vote': 0, 'restaurant': 6}}
        self.client.force_login(user=self.user)
        id = RestaurantModel.objects.all()[1].id
        response = self.client.post(reverse("upload-menu"),
                                    {"restaurant": id, "menu": "menu menu menu"},
                                    format='json')
        self.assertEquals(response.data, expected)

    def test_display_menu_list_view(self):
        response = self.client.get(reverse("menu"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
