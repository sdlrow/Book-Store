# Generated by Django 3.2.4 on 2021-12-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookShop', '0019_alter_cartproduct_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
