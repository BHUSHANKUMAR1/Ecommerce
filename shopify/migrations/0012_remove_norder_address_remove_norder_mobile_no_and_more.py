# Generated by Django 4.1.3 on 2022-11-23 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopify", "0011_alter_order_date_norder"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="norder",
            name="address",
        ),
        migrations.RemoveField(
            model_name="norder",
            name="mobile_no",
        ),
        migrations.AlterField(
            model_name="norder",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 23, 21, 41, 22, 864114)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 23, 21, 41, 22, 864114)
            ),
        ),
    ]
