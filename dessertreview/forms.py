from django.contrib.auth.models import User
from dessertreview.models import UserProfile, Review, Category, Shop, Dessert
from django import forms

# New user form

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("picture",)

#  Login form
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


# Review form
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='Category Name: ')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)
        
class ReviewForm(forms.ModelForm):
    dessert = forms.ModelChoiceField(queryset=Dessert.objects.all(), label='Dessert: ')
    name = forms.CharField(max_length=128, label='Title: ')
    text = forms.CharField(max_length=Dessert.TITLE_MAX_LENGTH, label='Review: ')

    class Meta:
        model = Review
        fields = ('dessert', 'name', 'text')


class DessertForm(forms.ModelForm):
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(), label='Shop: ')
    name = forms.CharField(max_length=128, label='Dessert Name: ')
    description = forms.CharField(max_length=Dessert.TITLE_MAX_LENGTH, label='Description: ')
    picture = forms.ImageField(label='Image: ')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category: ')

    class Meta:
        model = Dessert
        fields = ('shop', 'name', 'description', 'picture', 'category')

class ShopForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='Shop Name: ')
    lat = forms.FloatField(label='Latitude: ')
    lng = forms.FloatField(label='Longitude: ')
    picture = forms.ImageField(label='Image: ')

    class Meta:
        model = Shop
        fields = ('name', 'lat', 'lng', 'picture')
