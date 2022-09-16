# Generated by Django 4.1.1 on 2022-09-15 20:38

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmodel',
            name='address',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='restaurantmodel',
            name='contact_no',
            field=models.CharField(default='unknown', max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number is not correct', regex='/\\(?([0-9]{3})\\)?([ .-]?)([0-9]{3})\\2([0-9]{4})/')]),
        ),
        migrations.AlterField(
            model_name='restaurantmodel',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('menu', models.TextField(max_length=1000)),
                ('vote', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurantmodel')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
