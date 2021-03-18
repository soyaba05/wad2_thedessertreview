from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return HttpResponse("home page")

def register(request):
    registered=False
    
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
                return redirect(reverse('dessertreview:index'))
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
    return redirect(reverse('dessertreview:index'))
