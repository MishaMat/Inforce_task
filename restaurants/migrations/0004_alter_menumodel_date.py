# Generated by Django 4.1.1 on 2022-09-16 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_restaurantmodel_contact_no_votemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 16)),
        ),
    ]