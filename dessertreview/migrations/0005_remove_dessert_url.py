# Generated by Django 2.2.17 on 2021-03-22 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessertreview', '0004_auto_20210322_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='url',
        ),
    ]