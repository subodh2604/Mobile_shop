# Generated by Django 3.0.7 on 2020-06-30 14:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic=False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_buy_now_cart_models'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='buy_now',
            new_name='buy_mobile',
        ),
    ]
