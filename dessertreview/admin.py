from django.contrib import admin
from dessertreview.models import Shop, Dessert, UserProfile, Review
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Shop, ShopAdmin)
admin.site.register(Dessert)
admin.site.register(UserProfile)
admin.site.register(Review)