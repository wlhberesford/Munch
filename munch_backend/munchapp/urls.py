from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('menu/', views.home, name='munch-home'),
    path('menu/sage/', views.menu_sage, name="menu_sage"),
    path('menu/commons/', views.menu_commons, name="menu_commons"),
    path('menu/blitman/', views.menu_blitman, name="menu_blitman"),
    path('menu/barh/', views.menu_barh, name="menu_barh"),
    path('about/', views.about, name="about"),
]