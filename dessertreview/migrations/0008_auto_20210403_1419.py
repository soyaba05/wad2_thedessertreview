# Generated by Django 2.2.17 on 2021-04-03 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessertreview', '0007_remove_shop_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dessert',
            options={'ordering': ['category']},
        ),
    ]
