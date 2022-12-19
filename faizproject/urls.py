from django.contrib import admin
from django.urls import path, include
from shopping.views import update
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopping.urls'),name='shopping'),
    path('shopingyuk/', include('shopingyuk.urls'),name='shopingyuk'),
    path('shopingkuy/', include('shopingkuy.urls'),name='shopingkuy'),
    path('update/', update,name='update'),
]
