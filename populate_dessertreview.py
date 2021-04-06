import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'wad2_thedessertreview.settings')

import django
django.setup()
from dessertreview.models import Shop, Category, Dessert

def populate():
    categories=["Pancakes", "Waffles", "Crepes", "Sundaes", "Milshakes"]
    shops=[
        ["Flavas", 55.86926982012218, -4.274004072128909],
        ["Big Licks", 55.86211812556167, -4.280469284050763]
    ]
    desserts=[
        ["Flavas", "Sugar Waffle", "Tasty and sweet", "Waffles"]
    ]
    for cat in categories:
        add_cat(cat)

    for shop in shops:
        add_shop(shop[0],shop[1],shop[2])

def add_cat(name):
    c=Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_shop(name, lat, lng):
    s=Shop.objects.get_or_create(name=name, lat=lat, lng=lng)[0]
    s.save()

if __name__ == '__main__':
    populate()