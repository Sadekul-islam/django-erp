"""
Main URL Configuration
"""

# Django admin
from django.contrib import admin

# URL tools
from django.urls import path, include

# Django auth views
from django.contrib.auth import views as auth_views

# Core views
from core import views


urlpatterns = [

    # =================================================
    # Admin panel
    # =================================================
    path(

        'admin/',

        admin.site.urls

    ),

    # =================================================
    # Home page
    # =================================================
    path(

        '',

        views.home,

        name='home'

    ),

    # =================================================
    # Login page
    # =================================================
    path(

        'login/',

        auth_views.LoginView.as_view(

            template_name='login.html'

        ),

        name='login'

    ),

    # =================================================
    # Logout
    # =================================================
    path(

        'logout/',

        auth_views.LogoutView.as_view(),

        name='logout'

    ),

    # =================================================
    # Inventory URLs include
    # =================================================
    path(

        '',

        include('inventory.urls')

    ),

]