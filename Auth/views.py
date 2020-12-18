from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login_user(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(username=user_name, password=password)
            if user is not None:

                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, 'user name or password did not matched')
                return redirect('login')
    else:

        return redirect('home')
    return render(request, 'register/login.html')


def sigin_user(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('user_name')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password2 = request.POST.get('password')
            print(first_name, last_name, username, email, password, password2)

            if (first_name and last_name and username and email and password2 and password2) == '':
                return render(request, 'register/sign_up.html', {'fail': 'fields cannot be empty'})
            else:
                if password == password2:
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'username already exists')
                        return redirect('signin')
                    elif User.objects.filter(email=email).exists():
                        messages.error(request, 'email aleady exists')
                        return redirect('signin')
                    First_name = first_name.capitalize()
                    Last_name = last_name.capitalize()
                    user = User.objects.create_user(
                        username=username, password=password, first_name=First_name, last_name=Last_name, email=email)
                    user.save()
                    print('user created')
                    return redirect('home')
                else:
                    messages.error(request, 'password did not matched')
                    return redirect('signin')
    else:
        return redirect('home')

    return render(request, 'register/sign_up.html')


def logout_user(request):
    print('hi')
    logout(request)
    return redirect('login')
