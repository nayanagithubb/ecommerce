# Generated by Django 4.2.2 on 2023-08-09 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_remove_usermember_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
