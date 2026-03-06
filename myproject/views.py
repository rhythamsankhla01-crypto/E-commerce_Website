from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from . import urls
from auth_app.middleware import auth
from django.contrib.contenttypes.models import ContentType

from service.models import Service
from fresharrivals.models import freshArrivals
from Tshirtsapp.models import Tshirt
from Footwearapp.models import FootwearItems
from Denimapp.models import DenimItems
from Winterwearapp.models import Winterwearitems
from Reviewsapp.models import Reviews
from Cartapp.models import CartItem
from Poloitems.models import Poloitems



from django.contrib import messages

#Extras 




@auth
def add_to_cart(request, product_id):

    product = DenimItems.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_page");


@auth
def cart_page(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.subtotal()

    return render(request, "Cart/cart.html", {
        "cart_items": cart_items,
        "total": total
    })
# Create your views here.


#Extras-----------









# Main

def Main(request):
    reviews_Data = Reviews.objects.all().order_by('-id')[:10];

    data5 = {
        'reviews_Data' : reviews_Data,
    };
    return render(request,"main/main.html", data5);


# Home 

def home(request):
    servicesData = Service.objects.all();    #ascending = .orderby("service_title") for decending = .orderby("-service_title")

    data1 = {
        'servicesData': servicesData,
    }

    return render(request, "home/home.html",data1);


# About

def about(request):
    data = {
        'file': 'index',
        'title': 'Django page',
        'bdata': 'Django server',
        'clist': ['Python', 'Java', 'Javascript', 'Django'],
        'dlist': [10,45,28,83,80,4,6,7,8,54,23],
        'studentdata':[
            {'name': "Sam", 'phone': 847546473},
            {'name': "Rohan", 'phone':463736465},
    ]
}
    return render(request,"index.html", {'active': 'about'});



#Shirts

def shirts(request):
    return render(request, "Shirts/shirts.html", {'active': 'shirts'});


#T-Shirt

def t_shirts(request):
    tshirtData = Tshirt.objects.all();

    data2 = {
        'tshirtData': tshirtData,
    }
    
    return render(request,"T-Shirt/t-shirt.html" ,data2);
 
#Footwear

def footwear(request):

    footwearData = FootwearItems.objects.all();
    data3 = {
        'footwearData' : footwearData,
    }

    return render(request, "footwear/footwear.html",data3);


# Register


# def login(request):
#     finalans = 0;
#     try:
#          if request.method == "POST":
#             finalans = 0;
#             mobile = int(request.POST.get("mob_no"));
#             code = int(request.POST.get("otp"));
#             finalans = mobile + code;
            
#             data = {
#                 'mob_no':mobile,
#                 'otp':code,
#                 'output': finalans,
#             }

#             print(f"Mobile No: {mobile}");
#             print(f"OTP: {code}");
#             return HttpResponseRedirect("/exclusive/");
        
#     except:
#             pass

#     return render(request, "join/join.html", {'output':finalans});


# def ai_chat(request):
#     if request.method == 'post':
#         input_text = request.post.get('input_text');
#         print(input_text);
#     return render(request,'Ai/ai.html');


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST);
        if form.is_valid():
            user = form.save();
            login(request, user);
        return redirect('login');
        
    else:
        initial_data = {'username':"", 'password1':"", 'password2':""};
        form = UserCreationForm(initial = initial_data);

    return render(request, 'Registration/register.html', {'form': form});



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST);
        if form.is_valid():
            user = form.get_user();
            login(request, user);
        return redirect('home');
        
        
    else:
        initial_data = {"username":"", "password":"",};
        form = AuthenticationForm(initial = initial_data);

    return render(request, 'join/join.html', {'form': form});


def logout_view(request):
    logout(request);
    return redirect("login");


def polos(request):
    poloData = Poloitems.objects.all();

    data6 = {
        'poloData' : poloData,
    }
    return render(request, "Polos/polo.html", data6);

def store(request):
    return render(request, "Stores/stores.html");


def winterwear(request):

    winterwearData = Winterwearitems.objects.all();
    data4 = {
        'winterwearData' : winterwearData,
    };

    return render(request,'Winterwear/winterwear.html',data4);


#Denim
 
def denim(request):
    denimData = DenimItems.objects.all();
    denimData = {
        'denimData' : denimData,
    }
    
    if request.user.is_authenticated:
        print("User is logged in")
    else:
        print("User is NOT logged in")
    return render(request,"Denim/denim.html",denimData);



#Exclusive "Slider"
def exclusive(request):
    products = [
        {"exclusive":"EXCLUSIVE", "name": "Check Shirt", "price": 1599, "img": "images/slider1.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Utility Shirt", "price": 1449, "img": "images/slider2.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Oversized Hoodie", "price": 1999, "img": "images/slider3.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider4.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider5.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider6.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/polo3.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Polo t-Shirt", "price": 1599, "img": "images/polo7.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider8.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider9.webp"},
        {"exclusive":"EXCLUSIVE", "name": "Patchwork Shirt", "price": 1599, "img": "images/slider10.webp"},
    ]
    return render(request, 'Exclusive/exclusive.html', {"products": products});


def aboutus(request):
    return render(request,('Aboutus/aboutus.html', {'active': 'aboutus'}));


def freshArrival(request):
    freshArrival_data = freshArrivals.objects.all();
    data = {
        'freshArrival_data' : freshArrival_data,
    };

    return render(request, "fresh-arrivals/fresh-arrivals.html", data);



@auth
def profile_view(request):
    user = request.user
    profile = user.profile  # get related Profile

    if request.method == "POST":
        # Update User model
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()

        # Update Profile model
        profile.phone = request.POST.get('phone', profile.phone)
        profile.address = request.POST.get('address', profile.address)
        profile.dob = request.POST.get('dob', profile.dob)
        profile.location = request.POST.get('location', profile.location)
        profile.postal_code = request.POST.get('postal_code', profile.postal_code)
        profile.gender = request.POST.get('gender', profile.gender)

        # Update avatar if uploaded
        if request.FILES.get('avatar'):
            profile.avatar = request.FILES['avatar']

        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'Profile/profile.html', {'user': user, 'profile': profile})

def logout_view(request):
    logout(request)
    return redirect('login');


