from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    NAME_MAX_LENGTH = 128
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    picture = models.ImageField(upload_to='shop_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Dessert Shops'

    def __str__(self):
        return self.name

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Dessert(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='dessert_images', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dessert, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["category"]

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    REVIEW_MAX_LENGTH = 250

    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text


