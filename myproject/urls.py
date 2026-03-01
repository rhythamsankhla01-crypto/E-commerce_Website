"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
 
        path('admin/', admin.site.urls),
        path('', views.Main),



        path('login/', views.login_view, name="login"),
        path('register/',views.register_view, name="register"),
        path('logout/',views.logout_view, name="logout"),


        path('profile/', views.profile_view, name='profile'),
        path('logout/', views.logout_view, name='logout'),

        
        path('cart/', views.cart_page, name='cart_page'),
        path('add/<str:model_name>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
        # path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
        path('home/', views.home, name="home"),
        path('about/', views.about),
        path('denim/', views.denim),
        path('shirts/', views.shirts),
        path('t-shirt/',views.t_shirts),
        path('footwear/', views.footwear),
        path('polo/',views.polos),
        path('stores/',views.store),
        path('winterwear/',views.winterwear, name="winterwear"),
        path('exclusive/', views.exclusive),
        path('aboutus/', views.aboutus),
        path('fresh-arrivals/', views.freshArrival),
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT);