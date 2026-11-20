from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
            return redirect('dashboard')

        else:
            return render (request, "accounts/login.html", {
                'error' : "Inavalid Username or password"
            }) 


    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout_page(request):

    if request.method == "POST":
        logout(request)

    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(request, 'accounts/register.html', {
                'error': 'Passwords do not match'
            })


        if User.objects.filter(username=username).exists():

            return render(request, 'accounts/register.html', {
                'error': 'Username already exists'
            })

        if User.objects.filter(email=email).exists():

            return render(request, 'accounts/register.html', {
                'error': 'Email already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return render(request, 'accounts/register.html', {
            'success': 'Registration successful!'
        })

    return render(request, 'accounts/register.html')




def home(request):

    return render(request, 'accounts/home.html')


def products(request):

    all_products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        'products': all_products
    })
