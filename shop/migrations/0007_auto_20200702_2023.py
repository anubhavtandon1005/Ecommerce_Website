# Generated by Django 3.0.7 on 2020-07-02 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200702_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orders_id',
            new_name='order_id',
        ),
    ]
