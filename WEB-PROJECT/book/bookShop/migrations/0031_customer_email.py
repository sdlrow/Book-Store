# Generated by Django 3.2.4 on 2021-12-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookShop', '0030_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
    ]