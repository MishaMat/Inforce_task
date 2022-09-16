import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

telephone_num_regex = r'^[0-9\-\+]{9,15}$'


class RestaurantModel(models.Model):
    """Represents restaurant class model"""
    name = models.CharField(unique=True, max_length=40)
    rating = models.IntegerField(default=1,
                                 validators=[
                                     MaxValueValidator(100),
                                     MinValueValidator(1)
                                 ])
    contact_no = models.CharField(max_length=15,
                                  default='unknown',
                                  validators=[RegexValidator(
                                      regex=telephone_num_regex,
                                      message='Phone number is not correct',
                                  ),
                                  ])
    address = models.CharField(max_length=255, default='unknown')

    def __str__(self):
        return self.name


class MenuModel(models.Model):
    """Represents menu class model"""
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())
    menu = models.TextField(max_length=1000)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant.name + " " + str(self.date)


class EmployeeModel(models.Model):
    """Represents employee class model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class VoteModel(models.Model):
    """Represents vote class model"""
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    voted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.user.username} - {self.menu.restaurant.name} - {self.voted_at}'
