import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'wad2_thedessertreview.settings')

import django
django.setup()
from dessertreview.models import Shop, Category, Dessert

def populate():
    categories=["Pancakes", "Waffles", "Crepes", "Sundaes", "Milshakes"]
    for cat in categories:
        add_cat(cat)

def add_cat(name):
    c=Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    populate()