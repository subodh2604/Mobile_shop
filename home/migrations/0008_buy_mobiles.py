# Generated by Django 3.0.7 on 2020-06-30 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
 
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_delete_buy_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.TextField(max_length=250)),
                ('cart_models', models.ManyToManyField(to='home.mobile_spec')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
