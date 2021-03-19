from django.contrib import admin
from dessertreview.models import Shop, Dessert, UserProfile, Review, Category
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class DessertAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Shop, ShopAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Category, CategoryAdmin)