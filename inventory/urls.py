# URL path import
from django.urls import path

# views import
from .views import product_list


urlpatterns = [

    # Product list page
    path(

        'products/',

        product_list,

        name='product_list'
    ),

]