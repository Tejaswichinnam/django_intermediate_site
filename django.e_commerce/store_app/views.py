from django.shortcuts import render,redirect
from .services import scrape_flipkart

from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from store_app.models import Useradd,Contact
from django.contrib.auth.decorators import login_required


# Create your views here.

def mobiles(request):
    mb_list = scrape_flipkart()
    return render(request, "mobiles.html", {"mb_list": mb_list})



@login_required(login_url='login')
def products(request):
    return render(request,"base.html")


def contact(request):
    return render(request,"contact.html")


def login_user(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect("home")
    return render(request,"login.html")



def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c=User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"signup.html")






def logout_user(request):
    logout(request)
    return redirect("login")



def contact(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        mob_num=request.POST['mob_num']
        city=request.POST['city']
        feedback=request.POST['feedback']

        c=Contact(firstname=firstname,lastname=lastname,email=email,mob_num=mob_num,city=city,feedback=feedback)
        c.save()
        return redirect("home")
    return render(request,"contact.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def Becomeaseller(request):
    return render(request,"becomeseller.html")