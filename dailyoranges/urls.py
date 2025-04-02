"""
URL configuration for dailyoranges project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from main import views
from main.views import signup, login, logout, farmerlogin, farmerlogout

urlpatterns = [
    path('', views.home, name='home'),
    path('fundamentalsodagroecology', views.courseone, name='courseone'),
    path('payment', views.payment_page, name='payment_form'),
    path('contact', views.contact, name='contact'),
    path("services_payment/", views.services_payment, name="services_payment"),
    path("payment_success/", views.payment_success, name="payment_success"),  # Success page

    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', farmerlogin, name='login'),
    path('logout/', farmerlogout, name='logout'),

    path('trigger', views.trigger, name='trigger'),
    path('callback', views.callback, name='logout'),
]
