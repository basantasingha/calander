from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    # path('post',views.create_product_view,name='post'),
    path('pro',views.products_view,name='pro'),
    path('category',views.categories_view,name='category')   
]