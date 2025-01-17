from django.shortcuts import render, redirect
from dessertreview.forms import UserForm, UserProfileForm, DessertForm, ShopForm, CategoryForm, ReviewForm
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dessertreview.models import Category, Dessert, Shop, Review


# Create your views here.

def home(request):
    context_dict = {}
    categories = Category.objects.all()
    shops = Shop.objects.all()
    context_dict["categories"] = categories
    context_dict["shops"] = shops
    return render(request, 'dessertreview/home.html', context = context_dict)
    
def about_us(request):
    return render(request, 'dessertreview/about_us.html')

def register(request):
    registered=False
    print("1st")
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request,'dessertreview/register.html', context=context_dict )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('dessertreview:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'dessertreview/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('dessertreview:home'))

@login_required
def my_account(request):
    return render(request, 'dessertreview/my_account.html')

@login_required
def my_reviews(request):
    context_dict = {}
    reviews = Review.objects.filter(user=request.user)
    context_dict["reviews"] = reviews
    return render(request, 'dessertreview/my_reviews.html', context = context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        desserts = Dessert.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['desserts'] = desserts
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    # Go render the response and return it to the client.
    return render(request, 'dessertreview/category.html', context=context_dict)

def show_review(request, review_slug):
    contex_dict = {}
    try:
        review = Review.objects.get(slug=dessert_slug)
        context_dict['review'] = review

    except Review.DoesNotExist:
        context_dict['review'] = None

    return render(request, 'dessertreview/my_reviews.html', context=context_dict)

def show_dessert(request, dessert_slug):
    context_dict = {}

    try:
        dessert = Dessert.objects.get(slug=dessert_slug)
        reviews = Review.objects.filter(dessert=dessert)
        context_dict['dessert'] = dessert
        context_dict['reviews'] = reviews
    except Dessert.DoesNotExist:
        context_dict['dessert'] = None

    return render(request, 'dessertreview/dessert.html', context=context_dict)

def categories(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories
    return render(request, 'dessertreview/categories.html', context=context_dict)

def show_shop(request, shop_slug):
    context_dict = {}

    try:
        shop = Shop.objects.get(slug=shop_slug)
        desserts = Dessert.objects.filter(shop=shop)
        context_dict['shop'] = shop
        context_dict['desserts'] = desserts

    except Shop.DoesNotExist:
        context_dict['shop'] = None
        
    return render(request, 'dessertreview/shop.html', context=context_dict)

def shops(request):
    context_dict = {}
    shops = Shop.objects.all()
    context_dict['shops'] = shops
    return render(request, 'dessertreview/shops.html', context=context_dict)

def write_a_review(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.user = request.user
            review_item.save()
            return redirect(reverse('dessertreview:home'))
        else:
            print(form.errors)
            
    return render(request, 'dessertreview/write_a_review.html', {'form': form})             

def add_dessert(request):
    form = DessertForm()

    if request.method == 'POST':
        form = DessertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('dessertreview:home'))
        else:
            print(form.errors)

    return render(request, 'dessertreview/add_dessert.html', {'form': form})

def add_shop(request):
    form = ShopForm()

    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('dessertreview:home'))
        else:
            print(form.errors)

    return render(request, 'dessertreview/add_shop.html', {'form': form})

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('dessertreview:home'))
        else:
            print(form.errors)

    return render(request, 'dessertreview/add_category.html', {'form': form})
