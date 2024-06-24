from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('basket/',views.basket,name='basket'),
        path('contact/',views.contact,name='contact'),
        path('register/',views.register,name='register'),
        path('login/',views.login_view,name='login'),
        path('logout/',views.logout_view,name='logout'),
]
