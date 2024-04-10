from atexit import register
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('product.html',views.product,name="product"),
    path('milk.html',views.milk,name="milk"),
    path('bread.html',views.bread,name="bread"),
    path('register.html/',views.register,name="register"),
    path('logi.html/',views.login,name="login"),
    # path('register/', register.as_view(), name='register'),
    path('register/', views.register, name='register'),
    # path('buffalo_milk.html',views.buffalo_milk,name="buffalo_milk.html"),   
]