from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from inventory.views import product_list


urlpatterns = [

    path('', product_list),

    path('admin/', admin.site.urls),

    path(
        'products/',
        include('inventory.urls')
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

]