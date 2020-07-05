"""Ecommerce_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<int:mobile_pk>/specifications/',views.specifications,name='specifications'),
    path('<int:addmobile_pk>/add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('<int:remove_mobile_pk>/remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    path('carts/',views.carts,name='carts'),
    path('<int:buy_pk>/buy_now/',views.buy_now,name='buy_now'),
    path('<int:order_pk>/buy/',views.buy,name='buy'),
    path('search/',views.search,name="search")
       
]

urlpatterns += urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



















