# Generated by Django 4.1.3 on 2022-11-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopify", "0006_alter_signup_mobile_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="password",
            field=models.CharField(max_length=200),
        ),
    ]