# Generated by Django 3.0.7 on 2020-07-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200705_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
