# Generated by Django 2.2.17 on 2021-04-02 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessertreview', '0006_shop_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='owner',
        ),
    ]