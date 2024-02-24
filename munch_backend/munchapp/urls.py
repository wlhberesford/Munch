from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='munch-home'),
    path('menu/sage/', views.menu_sage, name="menu_sage"),
    path('about/', views.about, name="about"),
]