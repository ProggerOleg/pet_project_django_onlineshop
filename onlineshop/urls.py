from django.urls import path
from .views import *
from cart.views import cart_detail

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_us, name='about'),
    path('shop/', ShopHome.as_view(), name='shop'),
    path('addpage/', AddProduct.as_view(), name='addpage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('user_room/', cart_detail, name='user_cart'),
    path('shop/<slug:cat_slug>/', ShopCategory.as_view(), name='category'),
    path('category/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
